from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('pest', 'Pest Control'),
        ('irrigation', 'Irrigation Setup'),
        ('rental', 'Equipment Rental'),
        ('consult', 'Fertilizer Consultation'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='pest')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per hour or per acre")
    provider_name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, help_text="Link to a service image")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)

    def __str__(self):
        return self.name