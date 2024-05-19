from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Food, Consume
# Create your views here.


def index(request):
    food_list = Food.objects.all()

    if request.method == "POST":
        food = request.POST["food_consumed"]
        food_consume = Food.objects.get(name=food)
        user = request.user
        consume = Consume(user=user, food_consume=food_consume)
        consume.save()
        return redirect('food_list')
    else:
        user_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/food_list.html', {'food_list': food_list,
                                                    'user_food': user_food})
    

def delete_consume(request, id):
    delete_food = Consume.objects.get(id=id)
    if request.method == "POST":
        delete_food.delete()
        return redirect('/')
    return render(request, "myapp/delete_food.html")
