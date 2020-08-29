from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def Home(request):
    blogs = Blog.objects.filter(active=True,featured=True)[0:3] 
    context = {"blogs":blogs}
    return render(request,'istiak/base.html',context)

