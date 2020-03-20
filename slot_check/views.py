from django.shortcuts import render, redirect
from formnew.models import new_event
from django.contrib import messages


def slot(request):
    if request.method == "POST":
        id = request.POST["id"]
        print(id)
        slot = new_event.objects.filter(id=id).first()
        print(slot)
        if not slot:
            print("Not a valid")
            messages.info(request, 'Not a valid ID')
            return redirect("slot_check:slot_details")
        else:
            name = slot.name
            email = slot.email
            phone_no = slot.phone_no
            event = slot.event
            time_slot = slot.time_slot
            return render(request, "result.html", {'name': name, 'email': email, 'phone_no': phone_no, 'event': event, 'time_slot': time_slot})
    else:
        return render(request, "slot.html")
