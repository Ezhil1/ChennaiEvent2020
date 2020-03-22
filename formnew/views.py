from django.shortcuts import redirect, render
from .models import new_event
from django.contrib.auth.models import auth, User
# from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        # user = register.objects.filter(
        #   name=username, password=password).first()
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('formnew:enroll')
            # return render(request, 'enroll.html', {'name': username})
        else:
            messages.info(request, 'Account not found')
            return redirect('formnew:login')
    else:
        return render(request, 'login.html')


def registernew(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email_id = request.POST["email"]
        password = request.POST["password"]
        Confirm_password = request.POST["Confirm_password"]
        if password == Confirm_password:
            user = User.objects.create_user(username=name, password=password,
                                            email=email_id)
            user.save()
            return redirect('formnew:login')
        else:
            messages.info(request, 'Password Does not match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def form(request):
    return render(request, 'form.html')


@login_required(login_url="home")
def enroll(request):
    if request.method == 'POST':
        name = request.POST["name1"]
        email_id = request.POST["email"]
        phone_no = request.POST["phn_no"]
        event = request.POST["event"]
        timeslot = request.POST["Time_slot"]
        if new_event.objects.filter(email=email_id):
            messages.info(request, 'This email ID already used for enrollment')
            return redirect('formnew:enroll')
        else:
            eve = new_event(name=name, email=email_id,
                            phone_no=phone_no, event=event, time_slot=timeslot)
            eve.save()
            id1 = new_event.objects.get(email=email_id)
            id2 = id1.id
            print(id2)
            return render(request, 'enroll_submit.html', {'name': name, 'id': id2})
    else:
        return render(request, 'enroll.html')


@login_required(login_url="home")
def logout(request):
    name = request.user.username
    auth.logout(request)
    return render(request, "logout.html", {'name1': name})
