from django import forms
from . import models


class model_Form(forms.ModelForm):
    class Meta:
        model = models.newForm
        fields = "__all__"
        widgets = {
            "product_description": forms.Textarea(attrs={"rows": 3, "cols": 40}),
            "order_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "order_datetime": forms.DateTimeInput(
                format="%Y-%m-%d %H:%M:%S", attrs={"type": "datetime-local"}
            ),
            "order_time": forms.TimeInput(format="%H:%M:%S", attrs={"type": "date"}),
        }
