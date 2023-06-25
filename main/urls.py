from django.urls import path
from .views import home,about,delete_addblog,update_addblog,searchBlog,login_user,logout_user,registration
from . import views
urlpatterns=[
    path("",home,name="home"),
    path('about',about,name="about"),
    path("delete_addblog/<int:id>",delete_addblog,name="delete_addblog"),
    path("update_addblog/<int:id>",update_addblog,name="update_addblog"),
    path("q/",searchBlog,name="search"),
    path('show_detail/<int:id>/', views.show_detail, name='show_detail'),
    path("register", registration,name="register"),
    path("login", login_user,name="login"),
    path("logout", logout_user,name="logout")
]