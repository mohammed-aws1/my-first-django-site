from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect,get_object_or_404
from .forms import contact,Create_User,Add_post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Posts
import datetime


# Create your views here.
def start(requset):
    return redirect('home')

def home(request):
    posts = Posts.objects.all().order_by('-time_created')[:11]
    side_posts = Posts.objects.all().filter(tags__iexact='نعم')
    dict ={
        "posts":posts,
        "side_posts": side_posts,
    }
    return render(request,'index.html',dict)

def about(request):
    about = Posts.objects.all().filter(tags__iexact='نبذة')
    dict = {
        'about':about,
    }
    return render(request,'about.html',dict)

def TheContact(request):
    if request.user.is_authenticated :
        form = contact()
        if request.method =='POST':
            form = contact(request.POST or None)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            full_name = first_name+' '+last_name
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            if form.is_valid():
                send_mail(
                    'from ' + full_name + ':' + subject,
                    message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request,'تم ارسال البريد')
                return redirect('home')
            else:
                messages.error(request,'هناك خطأ في ايميلك او هناك حقول فارغة ')
        return render(request, 'contact.html', {'form': form})

    messages.warning(request,'يجب عليك تسجيل الدخول')
    return redirect('home')

def register(request):
    if not request.user.is_authenticated:
        form = Create_User()
        if request.method =='POST':
            form = Create_User(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                User.objects.create_user(username=username,email=email,password=password)
                messages.success(request,' تم انشاء الحساب')
                return redirect('login')

        dict ={
            'form':form,
        }
        return render(request,'register.html',dict)
    else:
        return redirect('home')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            username = request.POST["username"]
            if username.count(' ') == 1:
                firstname, lastname = username.split(' ')
                username = firstname + '_' + lastname
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'تم تسجيل الدخول')
                return redirect('home')
            else:
                messages.error(request,'الاسم او كلمة المرور غير صحيحة')
        return render(request,'login.html',{})
    else :
        return redirect('home')

@login_required()
def logout_view(request):
    logout(request)
    messages.success(request,'تم تسجيل الخروج')
    return redirect('home')

def content(request,id):
    post_site = Posts.objects.get(id=id)
    dict={
        'post_site':post_site,
    }
    return render(request,'post_site.html',dict)
@login_required()
def post_add(request):
    if request.user.is_staff:
        form = Add_post()
        if request.method == 'POST':
            form = Add_post(request.POST, request.FILES)
            if form.is_valid():
                form_name = form.save(commit=False)
                form_name.user = request.user
                form_name.time_created = datetime.datetime.now()
                form_name.save()
                return redirect('home')
        dict ={
            'form':form
        }
        return render(request,'add_page.html',dict)

@login_required()
def delete(request,id):
    if request.user.is_staff:
        post = Posts.objects.get(pk=id)
        post.delete()
        messages.success(request,' تم حذف المنشور ')
        return redirect('home')
