from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


CATIGORY_CHOISE=(
    
    ('ML','Milk'),
    ('CD','Curd'),
    ('LS','Lessi'),
    ('MK','Milkchaik'),
    ('PN','Panner'),
    ('GH','Ghee'),
    ('IC','Ice-crime'),
    
)

STATE_CHOISE=(
    
    ('sgASDgh','sdbvs'),
    ('sdbdb','sdbsdb'),
    ('sdvgsdgv','sdvbsd'),
    ('MdsvK','sdgv'),
    ('vcxb','gkh'),
    ('uhjgk','Ghrhtee'),
    ('srh','rh-rheth'),
    
)

class Products(models.Model):
    
    title = models.CharField(max_length=100,null=True,blank=True)
    selling_price = models.FloatField(null=True,blank=True)
    discoanted_price = models.FloatField(null=True,blank=True)
    discription = models.TextField(null=True,blank=True)
    composition = models.TextField(default='',null=True,blank=True)
    prodap = models.TextField(default='',null=True,blank=True)
    brand = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(choices=CATIGORY_CHOISE,max_length=2,null=True,blank=True)
    product_image = models.ImageField(upload_to='product',null=True,blank=True)

    def __str__(self):
        return self.title
    

class custem(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True,blank=True)
    locality = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField(default='0',null=True,blank=True)
    zipcode = models.IntegerField(default='0',null=True,blank=True)
    state = models.CharField(choices=STATE_CHOISE,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    
    
    
class Order(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default='1')
    ordred = models.BooleanField(default=False)
    ordred_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"
    


class Cart(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.username
    
    def delete(self , *args ,**kwargs):
        
        for order in self.orders.all():
            order.ordred = True
            order.ordred_date = timezone.now()
            order.save()
        
        self.orders.clear()
        super().delete(*args ,**kwargs)
    
