from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import EventCreationForm
from django.contrib import messages
from .models import Event, UsersCustomuser

# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {"form": form})

@login_required(login_url="/login")
def editprofile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Twój profil został zaaktualizowany!')
            return redirect('/home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})

@login_required(login_url="/login")
def addevent(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            currentuser = request.user
            event.user = UsersCustomuser.objects.get(id=currentuser.id)
            event.save()
            messages.success(request, "Dodano pomyślnie")
            return redirect('/home')
    else:
        form = EventCreationForm()

    return render(request, 'addevent.html', {"form": form})

@login_required(login_url="/login")
def editevent(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventCreationForm(request.POST, instance=event)
        if form.is_valid():
            event.save()
            messages.success(request, 'Zapisano zmiany')
            return redirect('/ownevents')
    else:
        form = EventCreationForm(instance=event)

    return render(request, 'editevent.html', {"form": form})


@login_required(login_url="/login")
def deleteevent(request, id):
    if request.method == 'POST':
        Event.objects.filter(id=id).delete()
        messages.success(request, "Usunięto pomyślnie")
        return redirect('/ownevents')
    return render(request, 'deleteevent.html')

@login_required(login_url="/login")
def showevents(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'showevents.html', context)

@login_required(login_url="/login")
def ownevents(request):
    currentuser = request.user
    events = Event.objects.filter(user=currentuser.id)
    context = {
        'events': events
    }
    return render(request, 'ownevents.html', context)

@login_required(login_url="/login")
def get_user_profile(request, id):
    profile = UsersCustomuser.objects.get(id=id)
    context = {
        'profile': profile
    }
    return render(request, 'showprofile.html', context)