from django import forms
from quizzy.models import Pub, Quiz, UserProfile
from django.contrib.auth.models import User

WEEKDAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)


class QuizForm(forms.ModelForm):
    categories = forms.CharField(help_text="Quiz categories:", required=False)
    weekday = forms.CharField(max_length=128, widget=forms.Select(choices=WEEKDAYS), help_text="Day:")
    time = forms.CharField(max_length=12, help_text="Start time (HH:MM):", required=False)
    prize = forms.CharField(help_text="Prizes to be won:", required=False)
    entry_fee = forms.IntegerField(help_text="Entry fee for this quiz:", required=False)

    upVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    downVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Quiz
        fields = ('categories', 'weekday', 'time', 'prize', 'entry_fee')
        exclude = ('pub',)


class PubForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Pub name:")
    street = forms.CharField(max_length=128, help_text="Street name:")
    street_number = forms.CharField(max_length=128, help_text="Street number:")
    postcode = forms.CharField(max_length=128, help_text="Postcode:")
    picture = forms.ImageField(required=False, help_text="Picture:")
    url = forms.URLField(max_length=300, help_text="Pub's webpage:", required=False)
    telephone = forms.CharField(max_length=128, help_text="Pub's phone number:", required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Pub
        fields = ('name', 'street', 'street_number', 'postcode', 'url', 'telephone', 'picture')
        exclude = ('city', )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
            'email': None,
            'password': "Your password can't be too similar to your other personal information and "
                        "must contain at least 8 characters and cannot be entirely numeric."
        }


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture', )
        exclude = ('user', 'favorites', 'ratedquizzes')
