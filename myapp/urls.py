from django.urls import path
from . import views
from myapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('bookcreate/',views.BookCreateView.as_view(),name='create'),
    path('bookdetail/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('signup/',views.SignupView.as_view(),name='signup')

]