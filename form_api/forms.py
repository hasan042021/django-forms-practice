from django import forms


class formAPI(forms.Form):

    is_active = forms.BooleanField(label="Is Active", required=False)

    first_name = forms.CharField(
        max_length=50,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}),
    )
    last_name = forms.CharField(
        max_length=50,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name"}),
    )

    is_published = forms.NullBooleanField(label="Is Published")

    time = forms.TimeField(label="Time", widget=forms.DateInput(attrs={"type": "date"}))
    favorite_color = forms.ChoiceField(
        choices=[("red", "Red"), ("green", "Green"), ("blue", "Blue")],
        label="Favorite Color",
    )

    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Price")

    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    profile_picture = forms.FileField(label="Profile Picture")

    rating = forms.FloatField(label="Rating")

    image = forms.ImageField(label="Image")

    quantity = forms.IntegerField(label="Quantity")

    ip_address = forms.GenericIPAddressField(label="IP Address")

    hobbies = forms.MultipleChoiceField(
        choices=[
            ("reading", "Reading"),
            ("traveling", "Traveling"),
            ("gaming", "Gaming"),
        ],
        label="Hobbies",
    )

    programming_languages = forms.TypedMultipleChoiceField(
        choices=[("python", "Python"), ("javascript", "JavaScript")],
        label="Programming Languages",
        coerce=str,
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    website = forms.URLField(label="Website")

    uuid = forms.UUIDField(label="UUID")
