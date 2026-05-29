from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import CategoryModelForm,ParticipantModelForm,EventModelForm
from django.contrib import messages
from events.models import Event, Category, Participant
def dashboard(request):
    event=Event.objects.all()
    return render(request,'dashboard.html',{'events':event})

def create_category(request):
    if request.method=='POST':
        form=CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Created Succesfully')
            return redirect('create-category')
    else:
        form=CategoryModelForm()
        
    context={'formss':form}
    return render(request,'category.html',context)


def create_participant(request):
    person=ParticipantModelForm()
    if request.method=='POST':
        person=ParticipantModelForm(request.POST)
        if person.is_valid():
            person.save()
            messages.success(request,'Paricipant Added Succesfully')
            return redirect('create-participant')
    context={'person':person}
    return render(request,'participant.html',context)


def create_event(request):
    event=EventModelForm()
    if request.method=='POST':
        event=EventModelForm(request.POST)
        if event.is_valid():
            event.save()
            messages.success(request,'Event Created Succesfully')
            return redirect('create-event')
        else:
            print(event.errors)
    context={'event':event}
    return render(request,'create_event.html',context)


def update(request):
    pass