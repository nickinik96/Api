from django.db import models

class Product (models.Model):
    title = models.CharField(max_length = 255) 
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)

class Customer (models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBERSHIP_GOLD = 'G'
    MEMEBERSHIP_CHOICES = [
        (MEMEBERSHIP_BRONZE,'Bronze'),
        (MEMEBERSHIP_SILVER,'Silver'),
        (MEMEBERSHIP_GOLD,'Gold')
        ]
    first_name = models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 15)
    birth_date= models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices=MEMEBERSHIP_CHOICES default=MEMEBERSHIP_SILVER) #B, S, G 

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    placed_status = [
        (STATUS_PENDING,'Pending'),
        (STATUS_COMPLETE,'Complete'),
        (STATUS_FAILED,'Failed') 
        ]
    placed_at = models.DateTimeField(auto_now_add=True)
    placed_status = models.CharField(max_length=1, default=PAYMENT_STATUS_PENDING)