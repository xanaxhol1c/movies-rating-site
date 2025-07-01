from django import forms
from .models import UserRatings

class RateMovieForm(forms.ModelForm):
    class Meta:
        model = UserRatings
        fields = ['score']

        widgets = {
            'score': forms.NumberInput(attrs={'min' : 1, 'max' : 10})
            }