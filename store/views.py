from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def store_home(request):
    """
    Displays the marketplace. 
    Synchronizes manual data with the database to ensure 'Like' works.
    """
    manual_products = [
        {'id': 1, 'name': 'Hybrid Wheat Seeds', 'category': 'seeds', 'price': 450, 'image': 'https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=500'},
        {'id': 2, 'name': 'NPK Fertilizer', 'category': 'fertilizer', 'price': 890, 'image': 'https://images.unsplash.com/photo-1628352081506-83c43123ed6d?w=500'},
        {'id': 3, 'name': 'Hand Cultivator', 'category': 'tools', 'price': 1200, 'image': 'https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?w=500'},
        {'id': 4, 'name': 'Power Tractor', 'category': 'equipments', 'price': 750000, 'image': 'https://5.imimg.com/data5/SELLER/Default/2022/9/PZ/WU/ZU/3501309/massey-ferguson-mf-7250-di-powerup-tractor-500x500.jpg'},
        {'id': 5, 'name': 'Organic Tomato Seeds', 'category': 'seeds', 'price': 150, 'image': 'https://images.unsplash.com/photo-1592982537447-7440770cbfc9?w=500'},
        {'id': 6, 'name': 'Liquid Nitrogen', 'category': 'fertilizer', 'price': 2200, 'image': 'https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=500'},
        {'id': 7, 'name': 'Garden Shovel', 'category': 'tools', 'price': 550, 'image': 'https://images.unsplash.com/photo-1589923188900-85dae523342b?w=500'},
        {'id': 8, 'name': 'Automated Sprinkler', 'category': 'equipments', 'price': 3500, 'image': 'https://i0.wp.com/indylawnmowerrecycle.com/wp-content/uploads/2024/02/sprinkler-system.jpeg?resize=720%2C500&ssl=1'},
        {'id': 9, 'name': 'Premium Rice Seeds', 'category': 'seeds', 'price': 600, 'image': 'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500'},
        {'id': 10, 'name': 'Electric Chain Saw', 'category': 'tools', 'price': 8500, 'image': 'https://www.chandakagro.com/upload/product/636930020107874961.png'},
    ]

    for p_data in manual_products:
        Product.objects.get_or_create(
            id=p_data['id'],
            defaults={
                'name': p_data['name'],
                'category': p_data['category'],
                'price': p_data['price'],
                
            }
        )

    query = request.GET.get('search', '').lower()
    category = request.GET.get('category', 'all')
    products = Product.objects.all()
    
    if category != 'all':
        products = products.filter(category=category)
    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'store/index.html', {'products': products})

# --- CART LOGIC ---

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        cart[p_id] += 1
    else:
        cart[p_id] = 1
    request.session['cart'] = cart
    return redirect('cart_page')

def cart_page(request):
    """Calculates subtotal per item and the final Grand Total."""
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0 # This variable must match your HTML: {{ grand_total }}
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        grand_total += subtotal # Accumulate the total
        
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total # Passed to template
    })

def update_cart_quantity(request, product_id, action):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    
    if p_id in cart:
        if action == 'increment':
            cart[p_id] += 1
        elif action == 'decrement':
            cart[p_id] -= 1
            if cart[p_id] <= 0:
                del cart[p_id]
                
    request.session['cart'] = cart
    return redirect('cart_page')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        del cart[p_id]
        request.session['cart'] = cart
    return redirect('cart_page')

# --- AUTH & SAVED ---

def toggle_save_product(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    product = get_object_or_404(Product, id=product_id)
    if request.user in product.saved_by.all():
        product.saved_by.remove(request.user)
        saved = False
    else:
        product.saved_by.add(request.user)
        saved = True
    return JsonResponse({'saved': saved})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def payment_page(request):
    """Displays the final payment options and total amount."""
    cart = request.session.get('cart', {})
    grand_total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        grand_total += product.price * quantity
        
    # If cart is empty, redirect back to store
    if not cart:
        return redirect('store_home')

    return render(request, 'store/payment.html', {
        'grand_total': grand_total
    })