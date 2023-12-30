# users/views.py
import random
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import LoveTest
from .forms import LoveCalculatorForm




def index(request):
    return render(request, 'users/index.html')


@csrf_exempt
# users/views.py

def love_calculator(request):
    love_percentage = None
    girl_name = None
    boy_name = None

    if request.method == 'POST':
        form = LoveCalculatorForm(request.POST)
        if form.is_valid():
            girl_name = form.cleaned_data['girl_name']
            boy_name = form.cleaned_data['boy_name']

            # Check if both names are in the database
            love_test_girl = LoveTest.objects.filter(girl_name=girl_name).first()
            love_test_boy = LoveTest.objects.filter(boy_name=boy_name).first()

            if love_test_girl and love_test_boy:
                # If both names are in the database, return the stored percentage
                love_percentage = love_test_girl.love_percentage
            else:
                # If names are not in the database, calculate the love percentage
                love_percentage = calculate_love_percentage(girl_name, boy_name)

                # Save data to the database
                love_test = LoveTest(girl_name=girl_name, boy_name=boy_name, love_percentage=love_percentage)
                love_test.save()

    else:
        form = LoveCalculatorForm()

    return render(request, 'users/test.html', {'form': form, 'love_percentage': love_percentage, 'girl_name': girl_name, 'boy_name': boy_name})




def calculate_love_percentage(girl_name, boy_name):

    

    if boy_name.lower() == "aavash":
        return random.randint(0, 20)
    else:
        return random.randint(50, 100)