from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def superadmin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ✅ Allow only superuser
            if user.is_superuser:
                login(request, user)
                return redirect("admin_dashboard")  # replace with your admin page name
            else:
                messages.error(request, "Access Denied! Only superusers can log in here.")
                return redirect("superadmin_login")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("superadmin_login")

    return render(request, "login.html")
from django.contrib.auth.decorators import login_required, user_passes_test

# ✅ Allow only superusers to access the dashboard
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, "admin.html")

def analytic(request):
    return render(request, "analytic.html")

from django.shortcuts import render

def admin_tracking(request):
    return render(request, "tracking.html")

from django.shortcuts import render

def animalid1(request):
    return render(request, 'animalid1.html')

def animalid2(request):
    return render(request, 'animalid2.html')

def animalid3(request):
    return render(request, 'animalid3.html')

def animalid4(request):
    return render(request, 'animalid4.html')

def animalid5(request):
    return render(request, 'animalid5.html')
from django.contrib import messages
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')
