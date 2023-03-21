from django.shortcuts import render
from rango.models import Category


from django.http import HttpResponse
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict = {'newsmessage1': 'According to the weather forecast, there will be heavy snow tomorrow which might cause some disruptions for the transportation.'}



    return render(request, 'rango/index.html', context=context_dict)

