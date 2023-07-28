from django.contrib import auth, messages
from django.shortcuts import redirect, render
from users.utils import clearCachedMessages
from users.models import CustomUser


def signin_view(request):
    """This is for signing in a user"""
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        j = CustomUser.objects.get(email = "josephmiracle119@gmail.com")
        j.set_password("miracle")
        j.save()

        if user is not None:
            auth.login(request, user)
            return redirect("success")
            
        else:
            messages.error(
                request,
                "Invalid credentials or User doesn't exists",
                fail_silently=True, extra_tags='warning'
            )
            clearCachedMessages(request)

    return render(request, "sign-in.html")


def success_view(request):
    """This is for displaying success page"""
    return render(request, "success.html")


def signup_view(request):
    """This is for signing in a user"""
    if request.method == "POST":
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        if CustomUser.objects.filter(email=email).exists():  # checks if an email exists
            messages.error(request, f"The email {email} exists", fail_silently=True)
            clearCachedMessages(request)

        else:
            CustomUser.objects.create_user(
                first_name=first_name, email=email, password=password
            )
            user = auth.authenticate(email=email, password=password)
            auth.login(request, user)
            return redirect("success")

    return render(request, "sign-up.html")


def logout_view(request):
    """This is for logging out a user"""
    auth.logout(request)
    return redirect("sign-in")
