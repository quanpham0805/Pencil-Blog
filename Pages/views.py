from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Pencil, PencilManufacturer, PencilType
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, template_name='home.html', context={"types": PencilType.objects.all})

def single_slug(request, single_slug):
    types = [valtype.type_slug for valtype in PencilType.objects.all()]
    if single_slug in types:
      return HttpResponse(f"{single_slug} is a type")

    pencils = [valpencil.pencil_slug for valpencil in Pencil.objects.all()]
    if single_slug in pencils:
      return HttpResponse(f"{single_slug} is a Pencil")

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")








def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("/")
        else:
            return render(request = request, template_name = "register.html", context = {"form": form})

    form = RegisterForm
    return render(request = request,
                  template_name = "register.html",
                  context = {"form": form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
                #messages.error(request, "Invalid username or password.")
        else:
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
            #messages.error(request, "Invalid username or password.")
    form = AuthenticationForm
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    #messages.info(request, "Logged out successfully!")
    return redirect("/")
