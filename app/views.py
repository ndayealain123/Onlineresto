from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 


def Home(request):
	menu_list = Menu.objects.all().order_by('-id')[:3]
	return render(request, "index.html", locals())

def Canteen(request):
	greet="how are you?"
	return render(request, "name.html",locals())

@login_required(login_url='/resto/login')
def finishOrder(request,pk):
	employee = Employee.objects.get(user=request.user)
	order = Order.objects.get(id=pk)
	order.vailable = True
	order.employee = employee
	order.save()
	return redirect(orderview)

@login_required(login_url='/resto/login')
def receiveOrder(request,pk):
	order = Order.objects.get(id=pk)
	order.delived = True
	order.save()
	return redirect(orderview)

@login_required(login_url='/resto/login')
def Create_order(request,pk):
	client = Client.objects.get(user=request.user)
	menu = Menu.objects.get(id=pk)
	order = Order(
		client = client,
		menu =menu
		)
	order.save()
	return redirect(orderview)

def Menuview(request):
	menu_list = Menu.objects.all()
	return render(request, "menu.html",locals())

def register_profil(request):
	profil_form=ProfileForm(request.POST or None, request.FILES)
	if (request.method=='POST'):
		if (profil_form.is_valid()):
			username=profil_form.cleaned_data['username']
			password=profil_form.cleaned_data['password']
			password1=profil_form.cleaned_data['password1']
			nom=profil_form.cleaned_data['nom']
			prenom=profil_form.cleaned_data['prenom']
			birthday=profil_form.cleaned_data['birthday']
			gender=profil_form.cleaned_data['gender']
			phone=profil_form.cleaned_data['phone']
			address=profil_form.cleaned_data['address']

			if (password==password1):
				user=User.objects.create_user(username=username, password=password)
				user.first_name=nom
				user.last_name=prenom
				user.save()
				group = Group.objects.get_or_create(name= "Client")
				user.groups.add(group[0])
				profil=Client(user=user,
						birthday=birthday,
						gender=gender,
						address=address,
						phone=phone).save()
				if user:
					login(request, user)
					return redirect(Home)
				else:
					return redirect(connexion)
			else: 
				profil_form=ProfileForm(request.FILES)
	profil_form=ProfileForm(request.FILES)
	return render(request, 'regester.html',locals())

def connexion(request):
	connexion_form=ConnexionForm(request.POST)
	if (request.method == 'POST'):
		if connexion_form.is_valid():
			username=connexion_form.cleaned_data['username']
			password=connexion_form.cleaned_data['password']
			user=authenticate(username=username,password=password)#verification donnée
			if user:#si l'objet existe 
				login(request, user)
				return redirect(Home) #on connecte l'utilisateur
			else:
				connexion_form=ConnexionForm()
	else:
		connexion_form=ConnexionForm()	
	return render(request, 'login.html', locals())

def deconnexion(request):
	logout(request)
	return redirect(Home)

@login_required(login_url='/resto/login')
def orderview(request):
	group = Group.objects.get(user=request.user)
	print(group)
	orderList = []
	group = str(group)
	if group == "Client":
		client = Client.objects.get(user=request.user)
		print(client)
		orderList = Order.objects.filter(client = client)
	
	elif group == "Chef":
		orderList = Order.objects.all()
	return render(request, "order.html",locals())

def Restoo(request):
	greet="how are you?"
	return render(request, "first.html",locals())


def aboutview(request):
	return render(request, "about.html",locals())
