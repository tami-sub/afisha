from django import forms

class NameForm (forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=True)
    password = forms.CharField(label='Your name', max_length=100, required=True)

    cinemaname = forms.CharField(label='Your name', max_length=100, required=True)
    cinemalocation = forms.CharField(label='Your name', max_length=100, required=True)
    cinemaid = forms.IntegerField(label='Your name', required=True)

    moviename = forms.CharField(label='Your name', max_length=100, required=True)
    jenre = forms.CharField(label='Your name', max_length=100, required=True)
    dimension = forms.IntegerField(label='Your name', required=True)
    timing = forms.IntegerField(label='Your name', required=True)
    directors = forms.CharField(label='Your name', max_length=100, required=True)
    actors = forms.CharField(label='Your name', max_length=100, required=True)
    schedule = forms.CharField(label='Your name', max_length=100, required=True)
    year = forms.IntegerField(label='Your name', required=True)

    time = forms.CharField(label='Your name', max_length=100, required=True)
    price = forms.IntegerField(label='Your name', required=True)
    day = forms.CharField(label='Your name', max_length=100, required=True)