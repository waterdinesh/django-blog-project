from django.shortcuts import render,redirect
from .models import Category,Addblog
from .forms import CategoryForm,UserForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


def home(request):
    print(request.user.id,"logged in user")
    
    addblog = Addblog.objects.all()
    categorys = Category.objects.annotate(blog_count=Count('addblog')) 
    latestposts = Addblog.objects.order_by("-date")[:3]
    paginator = Paginator(addblog, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', context={"addblog": page_obj, "category": categorys, 'page_obj': page_obj, "latestposts": latestposts})

    
@login_required
def about(request):
    user_id = request.user.id
    if request.method == 'POST':
        category_form = CategoryForm(request.POST,request.FILES)
        if category_form.is_valid():
            category_form.save()
    category_form = CategoryForm()
    categorys = Category.objects.all()
    addblog = Addblog.objects.filter(user=request.user)
    return render(request,'about.html', context={"category": categorys, "category_form": category_form,'addblog':addblog})

def delete_addblog(request,id):
    adb=Addblog.objects.get(id=id)
    adb.delete()
    return redirect('about')
@login_required
def update_addblog(request,id):
    instance=Addblog.objects.get(id=id)
    if request.method=="POST":
        category_form=CategoryForm(request.POST,instance=instance)
        if category_form.is_valid():
            category_form.save()
        return redirect('home')
    category_form=CategoryForm(instance=instance)
    addblog=Addblog.objects.all()
    return render(request,'update_addblog.html',context={'addblog':addblog,"category_form": category_form})

# Create your views here.
def searchBlog(request):
    query = request.GET.get("search")
    category_filter = request.GET.get("category")
    categorys = Category.objects.all()
    # latestposts = Latestpost.objects.all() 
    print(query)
    addblog = Addblog.objects.filter(Q(category__name__icontains=query)|Q(name__icontains=query))

    message = ""
    if not addblog.exists():
        message = "No matching results found."

    context = {
        'addblog': addblog,
        "category": categorys,
        'query': query,
        'category_filter': category_filter,
        'message': message,
        # "latestposts": latestposts
    }

    return render(request, "home.html", context)

def show_detail(request, id):
    addblog = [Addblog.objects.get(id=id)]  
    return render(request, 'show_detail.html', {'addblog': addblog})

def login_user(request):
    if request.method == 'POST':
        req = request.POST
        username = req.get('username')
        password = req.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('about')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            signup = user_form.save()
            signup.password = make_password(user_form.cleaned_data['password'])
            signup.save()
    user_form = UserForm()
    return render(request, 'registration.html',context={'form':user_form})



