from django.shortcuts import render
from . import forms


# Create your views here.
def form_api(request):
    form = forms.formAPI()
    return render(request, "form_api.html", {"form": form})
