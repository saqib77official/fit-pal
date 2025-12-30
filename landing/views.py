from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your feedback!')
            return redirect('home')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all()
    return render(
        request,
        'landing/index.html',
        {
            'form': form,
            'feedbacks': feedbacks,
        },
    )
