from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__ (self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    have = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', null=True,blank=True)


    def __str__(self):
        return self.product_name

