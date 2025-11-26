from django.urls import path
from . import views
from .views import search


app_name = 'make'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #検索サーチのurl
    path("search/", search, name="search"),
    path('make/', views.CreateMakeView.as_view(), name='make'),
    path('makes_done/', views.MakeSuccessView.as_view(), name='makes_done'),
    path('makes/<int:category>/', views.CategoryView.as_view(), name = 'makes_cat'),
    path('user-list/<int:user>/', views.UserView.as_view(), name='user_list'),
    path('makes-detail/<int:pk>/', views.DetailView.as_view(), name = 'makes_detail'),
    path('makes-delete/<int:pk>/', views.DetailView.as_view(), name = 'makes_delete'),
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    path('question/',views.QuestionView.as_view(),name='question'),
]