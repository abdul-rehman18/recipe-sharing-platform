from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Recipes,User,Category
from django.contrib import messages




def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipe_de')  
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')



def create_recipe(request):
    if request.method == 'POST':
        recipe = Recipes(
            RecipeName=request.POST['recipe_name'],
            Ingredients=request.POST['ingredients'],
            PreparationSteps=request.POST['preparation_steps'],
            DietaryInformation=request.POST['dietary_information'],
            CategoryID=int(request.POST['category_id'])
        )
        recipe.save()
        return redirect('recipe_de') 

    return render(request, 'create_recipe.html')


def create_catgeory(request):
    if request.method =='POST':
        category = Category(
            CategoryName= request.POST['categroy_name']
        )
        category.save()
        return redirect('recipe_de')
    return render(request,'create_category.html')


def signup(request):
    if request.method=='POST':
        user = User(
            Username=request.POST['username'],
            Email = request.POST['email'],
            Password = request.POST['password']
        )
        
    
        user.save()
        return redirect('category')

    return render(request,'signup.html')
