from django.shortcuts import render

#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from basicApp.forms import UserForm, UserProfileForm

def index(request):
    return render(request, "basicApp/index.html")



def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('basicApp:login'))
    return render(request, "basicApp/home.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your password doesnot match the username")

        else:
            print("Abi nah hacker?")

    else:
        return render(request, "basicApp/login.html")

def register(request):
    registered = False

    if request.method == "POST":
        userform = UserForm(data=request.POST)
        userProForm = UserProfileForm(request.POST, request.FILES)

        if userform.is_valid() and userProForm.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = userProForm.save(commit=False)
            profile.user = user

            if 'profilePics' in request.FILES:
                profile.userPic = request.FILES['profilePics']

            profile.save()

            registered = True

        else:
            print(userform.errors, userProForm.errors)

    else:
        userform = UserForm()
        userProForm = UserProfileForm()

    return render(request, "basicApp/registration.html", {
        "userform": userform, "userProForm": userProForm, "registered": registered
    })
# Create your views here.
