from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    image = models.FileField(upload_to="media/products/category", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Marque(models.Model):
    name = models.CharField(max_length=60)
    image = models.FileField(upload_to="media/products/marque")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Product(models.Model):
    image = models.ImageField(upload_to="media/products/product")
    name = models.CharField(max_length=60)
    screen = models.CharField(max_length=60, blank=True)
    cpu = models.CharField(max_length=60, blank=True)
    gpu = models.CharField(max_length=60, blank=True)
    ram = models.CharField(max_length=60, blank=True)
    space = models.CharField(max_length=60, blank=True)
    price = models.PositiveBigIntegerField(blank=True)
    description = models.TextField(blank=True)
    new = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_date']        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/products/product/images/")

    def __str__(self):
        return self.product.name