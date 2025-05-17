from django.db import models

class Product(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    product_name = models.CharField(max_length=100)
    product_model_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    warranty_date = models.DateField()
   

    def __str__(self):
        return f"{self.product_name} ({self.serial_number})"
