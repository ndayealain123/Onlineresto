from django.db import models
from django.contrib.auth.models import User  
from datetime import datetime

class Employee(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="employee_user")
	birthday =models.DateField(default=datetime.now)
	gender =models.CharField(max_length=100)
	phone =models.CharField(max_length=100)

class Client(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="client_user")
	birthday =models.DateField(default=datetime.now)
	gender =models.CharField(max_length=100, null = True)
	phone =models.CharField(max_length=100, null = True)
	address=models.CharField(max_length=100, null = True)
	
class Menu(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField(max_length=100)
	photos=models.ImageField(upload_to='Images/Menus/')
	price=models.PositiveIntegerField()

	def __str__(self):
		return f'Name:{self.name}--Price:{self.price}'

class Drink(models.Model):
	name=models.CharField(max_length=100)
	price=models.PositiveIntegerField()

class Order(models.Model):
	client=models.ForeignKey(Client,on_delete=models.CASCADE,null=True)
	menu=models.ForeignKey(Menu,on_delete=models.CASCADE,null=True)
	drink=models.ForeignKey(Drink,on_delete=models.CASCADE,null=True)
	vailable=models.BooleanField(default = False)
	delived=models.BooleanField(default = False)
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
	datetime=models.DateTimeField(default=datetime.now)


class DeliverOrder(models.Model):
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
	order=models.CharField(max_length=100)
	delived=models.BooleanField(default = False)
