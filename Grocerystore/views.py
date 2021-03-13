from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from  django.contrib.auth import authenticate,logout
from  django.contrib.auth import login
from .models import AddItem,ItemList
from django.contrib import messages
from .filters import AddItemfilter
from .forms import CreateUserForm,Additemform
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,"index.html")

def register(request):
	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()		
			return redirect('login')			
						
	else:
		form = CreateUserForm
	return render(request, "register.html", {'form':form})


@login_required(login_url='login')
def base(request):				
		Addeditem = request.user.itemlist.all()		
		my_filter = AddItemfilter(request.GET, queryset=Addeditem)
		Addeditem = my_filter.qs
		context ={'Addeditem':Addeditem,'AddItemfilter':my_filter}	
		return render(request, 'base.html',context)

	
def add(request):
	form = Additemform()
	if request.method=="POST":
		form = Additemform(request.POST)
		if form.is_valid():
			name = form.cleaned_data['item_name']	
			quantity = form.cleaned_data['item_quantity']
			status = form.cleaned_data['item_status']
			date  = form.cleaned_data['Date']			
			t = ItemList(item_name=name,item_quantity=quantity,item_status=status,Date=date)
			t.save()
			request.user.itemlist.add(t)										
			print("item added")
			messages.success(request, ("Item has been added to the basket!"))
			return redirect('base')
		else:
			return render(request, 'add.html',{'form':form})
	return render(request,'add.html',{'form':form})

def update(request,pk):
	Addeditem = ItemList.objects.get(id=pk)
	form = Additemform(instance=Addeditem)
	context = {"form":form}
	if request.method=='POST':
		form = Additemform(request.POST,instance=Addeditem)
		if form.is_valid():
			form.save()
			return redirect("base")
	return render(request, 'update.html',context)

def delete(request,pk):
	item = ItemList.objects.get(id=pk)
	context = {'item':item}
	if request.method=='POST':
		item.delete()
		return redirect('base')

	return render(request,"delete.html",context)

