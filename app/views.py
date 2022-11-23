from django.shortcuts import render,redirect
from .fifo import *
from .sjf import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def grafic(request):
    type_process = request.GET['type_process']
    number_process = request.GET['number_process']

    if type_process == 'FIFO':
        fifo(int(number_process))
    else:
        sjf(int(number_process))
    return redirect('/')
