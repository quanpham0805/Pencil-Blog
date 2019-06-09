from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Pencil, PencilManufacturer, PencilType
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request, template_name='home.html', context={"types": PencilType.objects.all})

def single_slug(request, single_slug):
    types = [valtype.type_slug for valtype in PencilType.objects.all()]
    if single_slug in types:
        TManufacturers = PencilManufacturer.objects.filter(manufacturer_for_type__type_slug=single_slug)
        manufacturerURL = {}

        for TVal in TManufacturers.all():
            temp = Pencil.objects.filter(pencil_for_manufacturer__manufacturer_name=TVal.manufacturer_name).earliest("pencil_published_date")
            manufacturerURL[TVal] = temp.pencil_slug

        return render(request=request, template_name='manufacturer.html', context={"temp": manufacturerURL})


    pencils = [valpencil.pencil_slug for valpencil in Pencil.objects.all()]
    if single_slug in pencils:
        TPencil = Pencil.objects.filter(pencil_slug=single_slug)
        return render(request=request, template_name="pencil.html", context={"pencils":TPencil})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid information")
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
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
        else:
            messages.error(request, "Invalid username or password.")
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
    form = AuthenticationForm
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def logout_request(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must log in to log out 😉")
        return redirect("/")

    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
