from django.db import models
import datetime
from django.contrib.auth.models import User

class ItemList(models.Model):
    item_name= models.CharField(max_length=20)
    item_quantity = models.CharField(max_length=5)
    item_status= models.CharField(max_length=20)
    
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="itemlist")
    Date = models.DateField(null=True)
    def __str__(self):
        return self.item_name

class AddItem(models.Model):
    itemlist= models.ForeignKey(ItemList,null=True, blank=True,on_delete=models.CASCADE)
    item_name= models.CharField(max_length=20)
    options= (("100gm","100gm"),("250gm","250gm"),('500gm',"500gm"),("750gm","750gm"),("1kg","1kg"),("2kg","2kg"),("3kg","3kg"),("4kg","4kg"),("5kg","5kg"),)
    item_quantity = models.CharField(max_length=5,choices=options)
    status=(("PENDING","pending"),("BOUGHT","bought"),("NOT AVAILABLE","not available"))
    item_status=models.CharField(max_length=20,choices=status,default='PENDING')
    Date = models.DateField(default=datetime.date.today)
    

    def __str__(self):
        return self.item_name

