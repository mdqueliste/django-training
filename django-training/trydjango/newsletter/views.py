from django.shortcuts import render

from .forms import SignUpForm

def home(request):
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }
    return render(request, "home.html", context)
