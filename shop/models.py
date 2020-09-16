from django.db import models

""" if change any thing makemigration and the use migrate """

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    subcategory = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    """ inside class we use method to return str value in perfect name """

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.IntegerField(max_length = 70,default="")
    desc = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name
         

    
