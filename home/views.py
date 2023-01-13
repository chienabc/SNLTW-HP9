from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import listItem
# Create your views here.
# def index(request):
#    list = listItemModel.objects.filter().order_by('listItem')
#    return render(request, 'pages/home.html')

def index(request):
  listItems = listItem.objects.all().values()
  template = loader.get_template('pages/home.html')
  context = {
    'mymembers': listItems,
  }
  return HttpResponse(template.render(context, request))


# def about(request):
#     return render(request, 'pages/about.html')

