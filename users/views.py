from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    '''Register a new user'''
    if request.method != "POST":
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process comleted form: register information into the form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to forum page
            login(request, new_user)
            return redirect('metta_forum:boards')

    '''Render the empty form or errors'''
    return render(request, "registration/register.html", {'form': form})
