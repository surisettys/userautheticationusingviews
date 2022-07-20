from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.models import Book,BookInstance,Genre,Author,Language
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView,DetailView
# Create your views here.
@login_required
def index(request):

    totalbooks = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_of_instance_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {'totalbooks':totalbooks,'num_instance':num_instance,'num_of_instances_avail':num_of_instance_avail}

    return render(request,'myapp/index.html',context= context)


class BookCreateView(LoginRequiredMixin,CreateView):

    model = Book
    fields = '__all__'

class BookDetailView(DetailView):
    model = Book

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'myapp/signup.html'
    
    