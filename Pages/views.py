# import the needed stuffs
# the views to configure, to communicate between model and user.

from django.shortcuts import render, redirect
from .form import RegisterForm, CommentForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Pencil, PencilManufacturer, PencilType, Comment
from django.http import HttpResponse
from django.contrib import messages


# below are the views

# homepage view:
def home(request):
    # render the request to home, using the template "home.html" in templates folder, and the parameter is types
	return render(request, template_name='home.html', context={"types": PencilType.objects.all})

# slug view for items
def single_slug(request, single_slug):
    # get all pencil type slug into array
    types = [valtype.type_slug for valtype in PencilType.objects.all()]

    # if the requested slug is in the array, i.e it is available
    if single_slug in types:
        # get the list of manufacturers that has the same type, using the unique slug. This is jumping from the child node to parent node.
        TManufacturers = PencilManufacturer.objects.filter(manufacturer_for_type__type_slug=single_slug)
        # define a dictionary to store data
        manufacturerURL = {}

        # iterate through data
        for TVal in TManufacturers.all():
            # get the pencils that have the same manufacturer, sort in oldest to newest order.
            temp = Pencil.objects.filter(pencil_for_manufacturer__manufacturer_name=TVal.manufacturer_name).earliest("pencil_published_date")
            # then the key is each manufacturer, and the value is the pencil_slug. The purpose is to get the slug
            manufacturerURL[TVal] = temp.pencil_slug

        # return render the manufacturer page
        return render(request=request, template_name='manufacturer.html', context={"temp": manufacturerURL})

    # get all pencil slug into array
    pencils = [valpencil.pencil_slug for valpencil in Pencil.objects.all()]
    # if the requested slug is in the array, i.e it is available
    if single_slug in pencils:
        # get the pencil that has the requested slug
        TPencil = Pencil.objects.get(pencil_slug=single_slug)
        # then get all pencils that have the same manufacturer, order oldest to latest
        allPencil = Pencil.objects.filter(pencil_for_manufacturer__manufacturer_name=TPencil.pencil_for_manufacturer).order_by('pencil_published_date')
        # get the comments for the post, order newest to oldest
        comments = Comment.objects.filter(comment_post__pencil_slug=TPencil.pencil_slug).order_by('-comment_published_date')
        # then render the page with the parameter we just got
        return render(request=request, template_name="pencil.html", context={"pencil":TPencil, "allPencil":allPencil, "comments":comments})

    # if we cannot find anything, then it is not available
    return HttpResponse(f"'{single_slug}' is not available on this page")

# function to add comment to the post
def add_comment(request, single_slug):
    # if the user is not logged in, he/she cannot comment
    if not request.user.is_authenticated:
        messages.error(request, "You must log in to comment")
        return redirect(f"/{single_slug}")

    # using POST to differentiate GET vs POST for commenting and requesting.
    if request.method == "POST":
        # using custom form in form.py for comments
        form = CommentForm(request.POST)
        # check if form valid
        if form.is_valid():
            # if it is valid
            # commit=False tells Django that "Don't send this to database yet.
            TComment = form.save(commit=False)
            # get the corresponding post for the comment
            TPost = Pencil.objects.get(pencil_slug=single_slug)
            # then assign value for it.
            TComment.comment_post = TPost
            TComment.comment_author = request.user
            # then push to the database
            TComment.save()
            # return back to the blog
            return redirect(f"/{single_slug}")
        else:
            # if there is an error
            messages.error(request, "An error has occur, please try again later 😭")
            return redirect("/")

    # if there is an error, just redirect back then send a message
    messages.error(request, "An error has occur, please try again later 😭")
    return redirect("/")

# function to register user
def register(request):
    # user try to access the page after logged in
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in 😉")
        return redirect('/')

    # using POST to differentiate GET vs POST for commenting and requesting.
    if request.method == "POST":
        # get the data using the custom form, with parameter is the request.
        form = RegisterForm(request.POST)
        if form.is_valid():
             # if it is valid then save
            user = form.save()
            username = form.cleaned_data.get('username')
            # get clean user name
            messages.success(request, f"New account created: {username}")
            # message that the account is created
            login(request, user)
            return redirect("/")
        else:
            # if form is not valid then tell the user it is invalid
            messages.error(request, "Invalid information")
            # render the page again.
            return render(request = request, template_name = "register.html", context = {"form": form})

    # first come here, use the form to render.
    form = RegisterForm
    return render(request = request,
                  template_name = "register.html",
                  context = {"form": form})

# function to log user in
def login_request(request):
    # user try to access the page after logged in
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in 😉")
        return redirect('/')

    # using POST to differentiate GET vs POST for commenting and requesting.
    if request.method == 'POST':
        # get the data using the django form, with parameter is the request.
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # if it is valid then check if there is such user in the database
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # if user exist
            if user is not None:
                # login and success message
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                # return back to main page
                return redirect('/')
            else:
                # not valid then return back to login page
                messages.error(request, "Invalid username or password.")
                return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
        else:
            # not valid then return back to login page
            messages.error(request, "Invalid username or password.")
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

    #first come here then use the authentication form to render the page
    form = AuthenticationForm
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

# funtion to log user out
def logout_request(request):
    # not log in but try to log out -> warning message
    if not request.user.is_authenticated:
        messages.warning(request, "You must log in to log out 😉")
        return redirect("/")

    # then logout and message that log out successfully
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

# function to view the profile
def view_profile(request, user):
    # if user is not log in, he/she can't see
    if not request.user.is_authenticated:
        messages.error(request, "You must log in to see this page")
        return redirect("/")

    # get the comments and posts belong to them
    comments = Comment.objects.filter(comment_author__username=request.user.username).order_by('-comment_published_date')
    posts = Pencil.objects.filter(pencil_author__username=request.user.username).order_by('-pencil_published_date')
    # then render the page
    return render(request=request, template_name="profile.html", context={"user":request.user, "comments":comments, "posts":posts})

