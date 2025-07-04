from django import forms
from .models import UserRatings

class RateMovieForm(forms.ModelForm):
    class Meta:
        model = UserRatings
        fields = ['score', 'review']

        widgets = {
            'score': forms.NumberInput(attrs={'min' : 1, 'max' : 10}),
            'review': forms.Textarea(attrs={'maxlength' : 250})
            }
        
    def clean_score(self):
        score = self.cleaned_data.get('score')

        if score is None or (score < 1 or score > 10):
            raise forms.ValidationError('Rating has to be in range(1-10)')
        return score
    
    def clean_review(self):
        review = self.cleaned_data.get('review')

        if review and len(review.strip()) > 250:
            raise forms.ValidationError('Review length can`t be bigger than 250 chars.')
        return review

