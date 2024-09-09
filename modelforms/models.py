from django.db import models


# Create your models here.


class newForm(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    customer_email = models.EmailField()
    product_url = models.URLField()
    product_slug = models.SlugField()
    customer_ip_address = models.GenericIPAddressField()  # Corrected based on error
    product_quantity = models.PositiveIntegerField()  # Ensures positive quantity
    product_quantity_small = models.SmallIntegerField()  # Ensures positive quantity
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_price_decimal = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    order_datetime = models.DateTimeField()
    order_time = models.TimeField()
    is_active = models.BooleanField(null=True, blank=True)  # Corrected based on error
    product_image = models.ImageField(upload_to="images/")
    product_image_file = models.FileField(upload_to="images/")

    def __str__(self):
        return self.title
