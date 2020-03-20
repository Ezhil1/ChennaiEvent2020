from django.shortcuts import redirect, render
from .models import register
from .models import new_event
from django.contrib.auth.models import auth, User
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        reg = register.objects.filter(name=username, password=password).first()
        if reg is not None:
            request.session
            return redirect('formnew:enroll')
        else:
            return redirect('formnew:login')
        # print("reg is ")
        # print(reg)
        # if reg is not None:
        #   auth.login(request, reg)
        #  print("user found")
        # return redirect("/")
        return render(request, 'register.html')

    else:
        return render(request, 'login.html')


def registernew(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email_id = request.POST["email"]
        password = request.POST["password"]
        Confirm_password = request.POST["Confirm_password"]
        if password == Confirm_password:
            reg = register(name=name, password=password,
                           confirm_password=Confirm_password, mail_id=email_id)
            reg.save()
            return redirect('formnew:login')
        else:
            messages.info(request, 'Password Does not match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def form(request):
    return render(request, 'form.html')


def enroll(request):
    if request.method == 'POST':
        name = request.POST["name1"]
        email_id = request.POST["email"]
        phone_no = request.POST["phn_no"]
        event = request.POST["event"]
        timeslot = request.POST["Time_slot"]
        if new_event.objects.filter(email=email_id):
            messages.info(request, 'Email taken')
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
