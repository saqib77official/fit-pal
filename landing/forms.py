from django import forms

from .models import Feedback, WaitlistEntry

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


class WaitlistForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={'placeholder': 'Get updates - your email', 'autocomplete': 'email'}
            ),
        }
