from django.shortcuts import render
from .models import Service

def services_list(request):
    # 1. Get filter data from URL
    selected_cat = request.GET.get('category', 'all')
    max_price = request.GET.get('price', '5000')

    # 2. Hardcoded data matching your request with suitable images
    all_services = [
        {'name': 'Drone Pest Control', 'category': 'pest', 'category_name': 'Pest Control', 'price': 500, 'provider': 'SkySpray Solutions', 'rating': '4.9', 'image': 'https://images.unsplash.com/photo-1586771107445-d3ca888129ff?w=800', 'desc': 'Aerial spraying for efficient and wide-coverage pest control using advanced drones.'},
        {'name': 'Organic Pest Management', 'category': 'pest', 'category_name': 'Pest Control', 'price': 350, 'provider': 'BioProtect', 'rating': '4.7', 'image': 'https://images.unsplash.com/photo-1592919016327-519289299b62?w=800', 'desc': 'Environmentally friendly pest solutions using natural biological deterrents.'},
        {'name': 'Drip Irrigation Install', 'category': 'irrigation', 'category_name': 'Irrigation Setup', 'price': 2500, 'provider': 'WaterFlow Systems', 'rating': '4.8', 'image': 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?w=800', 'desc': 'Complete installation of water-efficient drip systems tailored to your crop layout.'},
        {'name': 'Smart Sensor Network', 'category': 'irrigation', 'category_name': 'Irrigation Setup', 'price': 1200, 'provider': 'AgriLink Tech', 'rating': '4.6', 'image': 'https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=800', 'desc': 'IoT-enabled sensors to monitor soil moisture levels in real-time.'},
        {'name': 'Harvester Rental', 'category': 'rental', 'category_name': 'Equipment Rental', 'price': 1500, 'provider': 'FarmGear Hub', 'rating': '4.9', 'image': 'https://images.unsplash.com/photo-1594398044700-011ca8877e42?w=800', 'desc': 'Modern harvest machinery available for daily or weekly rental periods.'},
        {'name': 'Tractor & Plough Set', 'category': 'rental', 'category_name': 'Equipment Rental', 'price': 800, 'provider': 'HeavyAgri Rentals', 'rating': '4.5', 'image': 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800', 'desc': 'High-torque tractors equipped with heavy-duty ploughing attachments.'},
        {'name': 'Soil Health Roadmap', 'category': 'consult', 'category_name': 'Fertilizer Consultation', 'price': 200, 'provider': 'NutriGrow Labs', 'rating': '4.8', 'image': 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=800', 'desc': 'Detailed laboratory analysis and 12-month nutrient management plan.'},
        {'name': 'NPK Balance Advisory', 'category': 'consult', 'category_name': 'Fertilizer Consultation', 'price': 150, 'provider': 'GreenYield Experts', 'rating': '4.4', 'image': 'https://images.unsplash.com/photo-1628352081506-83c43123ed6d?w=800', 'desc': 'Expert advice on optimizing Nitrogen, Phosphorus, and Potassium levels.'},
    ]

    # 3. Filtering Logicfrom django.shortcuts import render

def services_list(request):
    # 1. Get filter data from URL
    selected_cat = request.GET.get('category', 'all')
    max_price = request.GET.get('price', '5000')

    # 2. Updated data with NEW images and descriptions
    all_services = [
        {
            'name': 'Drone Pest Control', 
            'category': 'pest', 
            'category_name': 'Pest Control', 
            'price': 500, 
            'provider': 'SkySpray Solutions', 
            'rating': '4.9', 
            'image': 'https://images.unsplash.com/photo-1586771107445-d3ca888129ff?w=800', 
            'desc': 'Aerial spraying for efficient and wide-coverage pest control using advanced agricultural drones.'
        },
        {
            'name': 'Organic Pest Management', 
            'category': 'pest', 
            'category_name': 'Pest Control', 
            'price': 350, 
            'provider': 'BioProtect', 
            'rating': '4.7', 
            'image': 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=800', 
            'desc': 'Environmentally friendly pest solutions using natural biological deterrents and organic sprays.'
        },
        {
            'name': 'Drip Irrigation Install', 
            'category': 'irrigation', 
            'category_name': 'Irrigation Setup', 
            'price': 2500, 
            'provider': 'WaterFlow Systems', 
            'rating': '4.8', 
            'image': 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?w=800', 
            'desc': 'Complete installation of water-efficient drip systems tailored to your crop layout.'
        },
        {
            'name': 'Smart Sensor Network', 
            'category': 'irrigation', 
            'category_name': 'Irrigation Setup', 
            'price': 1200, 
            'provider': 'AgriLink Tech', 
            'rating': '4.6', 
            'image': 'https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=800', 
            'desc': 'IoT-enabled sensors to monitor soil moisture levels in real-time across your fields.'
        },
        {
            'name': 'Harvester Rental', 
            'category': 'rental', 
            'category_name': 'Equipment Rental', 
            'price': 1500, 
            'provider': 'FarmGear Hub', 
            'rating': '4.9', 
            'image': 'https://images.pexels.com/photos/2933243/pexels-photo-2933243.jpeg?auto=compress&cs=tinysrgb&w=800', # NEW reliable image
            'desc': 'Modern harvest machinery available for daily or weekly rental periods during peak season.'
        },
        {
            'name': 'Tractor & Plough Set', 
            'category': 'rental', 
            'category_name': 'Equipment Rental', 
            'price': 800, 
            'provider': 'HeavyAgri Rentals', 
            'rating': '4.5', 
            'image': 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800', 
            'desc': 'High-torque tractors equipped with heavy-duty ploughing attachments for soil preparation.'
        },
        {
            'name': 'Soil Health Roadmap', 
            'category': 'consult', 
            'category_name': 'Fertilizer Consultation', 
            'price': 200, 
            'provider': 'NutriGrow Labs', 
            'rating': '4.8', 
            'image': 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=800', 
            'desc': 'Detailed laboratory analysis and 12-month nutrient management plan for optimal growth.'
        },
        {
            'name': 'NPK Balance Advisory', 
            'category': 'consult', 
            'category_name': 'Fertilizer Consultation', 
            'price': 150, 
            'provider': 'GreenYield Experts', 
            'rating': '4.4', 
            'image': 'https://images.unsplash.com/photo-1628352081506-83c43123ed6d?w=800', # NEW reliable image
            'desc': 'Expert advice on optimizing Nitrogen, Phosphorus, and Potassium levels in your soil.'
        },
    ]

    # Filtering Logic
    filtered_services = []
    for s in all_services:
        cat_match = (selected_cat == 'all' or s['category'] == selected_cat)
        price_match = (s['price'] <= int(max_price))
        if cat_match and price_match:
            filtered_services.append(s)

    context = {
        'services': filtered_services,
        'selected_category': selected_cat,
        'max_price': max_price,
        'categories': [
            ('pest', 'Pest Control'),
            ('irrigation', 'Irrigation Setup'),
            ('rental', 'Equipment Rental'),
            ('consult', 'Fertilizer Consultation'),
        ]
    }
    return render(request, 'services/index.html', context)

    filtered_services = []
    for s in all_services:
        # Check category
        cat_match = (selected_cat == 'all' or s['category'] == selected_cat)
        # Check price
        price_match = (s['price'] <= int(max_price))
        
        if cat_match and price_match:
            filtered_services.append(s)

    context = {
        'services': filtered_services,
        'selected_category': selected_cat,
        'max_price': max_price,
        'categories': [
            ('pest', 'Pest Control'),
            ('irrigation', 'Irrigation Setup'),
            ('rental', 'Equipment Rental'),
            ('consult', 'Fertilizer Consultation'),
        ]
    }
    return render(request, 'services/index.html', context)

# Add this new function to your existing views.py

def service_contact(request, service_name):
    # This is the same list from your main view
    all_services = [
        {'name': 'Drone Pest Control', 'category': 'pest', 'category_name': 'Pest Control', 'price': 500, 'provider': 'SkySpray Solutions', 'rating': '4.9', 'image': 'https://images.unsplash.com/photo-1586771107445-d3ca888129ff?w=800', 'contact_info': '99887-76655'},
        {'name': 'Organic Pest Management', 'category': 'pest', 'category_name': 'Pest Control', 'price': 350, 'provider': 'BioProtect', 'rating': '4.7', 'image': 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=800', 'contact_info': '88776-65544'},
        {'name': 'Drip Irrigation Install', 'category': 'irrigation', 'category_name': 'Irrigation Setup', 'price': 2500, 'provider': 'WaterFlow Systems', 'rating': '4.8', 'image': 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?w=800', 'contact_info': '77665-54433'},
        {'name': 'Smart Sensor Network', 'category': 'irrigation', 'category_name': 'Irrigation Setup', 'price': 1200, 'provider': 'AgriLink Tech', 'rating': '4.6', 'image': 'https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=800', 'contact_info': '66554-43322'},
        {'name': 'Harvester Rental', 'category': 'rental', 'category_name': 'Equipment Rental', 'price': 1500, 'provider': 'FarmGear Hub', 'rating': '4.9', 'image': 'https://images.pexels.com/photos/2933243/pexels-photo-2933243.jpeg?auto=compress&cs=tinysrgb&w=800', 'contact_info': '55443-32211'},
        {'name': 'Tractor & Plough Set', 'category': 'rental', 'category_name': 'Equipment Rental', 'price': 800, 'provider': 'HeavyAgri Rentals', 'rating': '4.5', 'image': 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800', 'contact_info': '44332-21100'},
        {'name': 'Soil Health Roadmap', 'category': 'consult', 'category_name': 'Fertilizer Consultation', 'price': 200, 'provider': 'NutriGrow Labs', 'rating': '4.8', 'image': 'https://images.unsplash.com/photo-1628352081506-83c43123ed6d?w=800', 'contact_info': '33221-10099'},
        {'name': 'NPK Balance Advisory', 'category': 'consult', 'category_name': 'Fertilizer Consultation', 'price': 150, 'provider': 'GreenYield Experts', 'rating': '4.4', 'image': 'https://images.pexels.com/photos/5946101/pexels-photo-5946101.jpeg?auto=compress&cs=tinysrgb&w=800', 'contact_info': '22110-09988'},
    ]
    
    # Find the specific service from the list
    service = next((item for item in all_services if item["name"] == service_name), None)
    
    return render(request, 'services/service_detail.html', {'service': service})