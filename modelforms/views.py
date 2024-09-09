from django.shortcuts import render
from . import forms


# Create your views here.
def model_forms(request):
    form = forms.model_Form()
    return render(request, "modelforms.html", {"form": form})
