from django.shortcuts import render, redirect, get_object_or_404
from .models import SeasonalFlavor, IngredientInventory, CustomerFeedback
from django.http import HttpResponse

def home(request):
    return render(request, 'management/home.html')


# Seasonal Flavor Views
def list_seasonal_flavors(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'management/seasonal_flavors.html', {'flavors': flavors})


def add_seasonal_flavor(request):
    if request.method == 'POST':
        flavor_name = request.POST.get('flavor_name')
        available_until = request.POST.get('available_until')
        SeasonalFlavor.objects.create(flavor_name=flavor_name, available_until=available_until)
        return redirect('list_seasonal_flavors')
    return render(request, 'management/add_seasonal_flavor.html')


def update_seasonal_flavor(request, flavor_id):
    flavor = get_object_or_404(SeasonalFlavor, id=flavor_id)
    if request.method == 'POST':
        flavor.flavor_name = request.POST.get('flavor_name')
        flavor.available_until = request.POST.get('available_until')
        flavor.save()
        return redirect('list_seasonal_flavors')
    return render(request, 'management/update_seasonal_flavor.html', {'flavor': flavor})


def delete_seasonal_flavor(request, flavor_id):
    flavor = get_object_or_404(SeasonalFlavor, id=flavor_id)
    flavor.delete()
    return redirect('list_seasonal_flavors')


# Customer Feedback Views
def list_feedback(request):
    feedback = CustomerFeedback.objects.all()
    return render(request, 'management/customer_feedback.html', {'feedback': feedback})


def add_feedback(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        suggestion = request.POST.get('suggestion')
        allergy_concern = request.POST.get('allergy_concern')
        CustomerFeedback.objects.create(
            customer_name=customer_name, 
            suggestion=suggestion, 
            allergy_concern=allergy_concern
        )
        return redirect('list_feedback')
    return render(request, 'management/add_feedback.html')

# Ingredient Inventory Views
def list_ingredients(request):
    ingredients = IngredientInventory.objects.all()
    return render(request, 'management/ingredients.html', {'ingredients': ingredients})


def add_ingredient(request):
    if request.method == 'POST':
        ingredient_name = request.POST.get('ingredient_name')
        quantity = request.POST.get('quantity')
        IngredientInventory.objects.create(ingredient_name=ingredient_name, quantity=quantity)
        return redirect('list_ingredients')
    return render(request, 'management/add_ingredient.html')


def update_ingredient(request, ingredient_id):
    ingredient = IngredientInventory.objects.get(id=ingredient_id)
    if request.method == 'POST':
        ingredient.ingredient_name = request.POST.get('ingredient_name')
        ingredient.quantity = request.POST.get('quantity')
        ingredient.save()
        return redirect('list_ingredients')
    return render(request, 'management/update_ingredient.html', {'ingredient': ingredient})


def delete_ingredient(request, ingredient_id):
    ingredient = IngredientInventory.objects.get(id=ingredient_id)
    ingredient.delete()
    return redirect('list_ingredients')
