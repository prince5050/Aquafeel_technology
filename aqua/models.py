import datetime

from django.db import models

# Create your models here.

class common_contact(models.Model):  # COMM0N Abstract table
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Product(models.Model):
    pro_status = ((1, 'Active'), (2, 'Deactivate'), (3, 'Delete'))
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    describe_1 = models.TextField(blank=True, null=True)
    describe_2 = models.TextField(blank=True, null=True)
    describe_3 = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='upload/product_image')
    price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=pro_status, default=1)

    def __str__(self):
        return self.name

class Contact(common_contact):
    contact_status = ((1, 'From Contact Page'), (2, 'From About Page'), (3, 'From Service Page'))
    request_from = models.CharField(max_length=100, choices=contact_status, default=0)

    def __str__(self):
        return self.name

class Qutation_for_product(common_contact):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name