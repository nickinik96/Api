from django.db import models
class  Promotion (models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()
    # products_set (IN THIS CODE products) -> promotion    => ALL THE PRODUCT THAT PROMOTION APPLY TO THEM

class Collection(models.Model):
    title = models.CharField(max_length = 255) 
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name = '+')

class Product (models.Model):
    title = models.CharField(max_length = 255)
    slag = models.SlugField()
    #slag = models.SlugField(default='-')
    #slag = models.SlugField(null = True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion, related_name='products')

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
    membership = models.CharField(max_length = 1, choices=MEMEBERSHIP_CHOICES, default=MEMEBERSHIP_SILVER) #B, S, G 
    class Meta:
        #db_table = 'store_Customers'
        indexes= [models.Index(fields=['last_name', 'first_name'])]

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    placed_status = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed') 
        ]
    placed_at = models.DateTimeField(auto_now_add = True)
    placed_status = models.CharField(max_length=1, default=PAYMENT_STATUS_PENDING)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)

class Address(models.Model): 
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10, default='00000')
    #customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key = True)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

class CardItem(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
