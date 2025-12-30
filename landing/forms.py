from django import forms

from .models import Feedback

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Your name', 'autocomplete': 'name'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'yourname@email.com', 'autocomplete': 'email'}
            ),
            'rating': forms.RadioSelect(choices=RATING_CHOICES),
            'message': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Share your feedback'}
            ),
        }
