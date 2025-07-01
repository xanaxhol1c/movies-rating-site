from django import forms
from .models import UserRatings

class RateMovieForm(forms.ModelForm):
    class Meta:
        model = UserRatings
        fields = ['score']

        widgets = {
            'score': forms.NumberInput(attrs={'min' : 1, 'max' : 10})
            }
    def clean_score(self):
        score = self.cleaned_data.get('score')

        if score is None or (score < 1 or score > 10):
            raise forms.ValidationError('Rating has to be in range(1-10)')
        return score
