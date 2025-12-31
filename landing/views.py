from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FeedbackForm, WaitlistForm
from .models import Feedback


def home(request):
    waitlist_form = WaitlistForm()
    form = FeedbackForm()
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'waitlist':
            waitlist_form = WaitlistForm(request.POST)
            if waitlist_form.is_valid():
                waitlist_form.save()
                messages.success(
                    request,
                    'Thanks! We will notify you and wish you a Happy New Year 2026.',
                    extra_tags='waitlist',
                )
                return redirect('home')
        else:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Your response has been saved. We appreciate your support and energy.',
                    extra_tags='feedback',
                )
                return redirect('home')

    feedbacks = Feedback.objects.all()
    return render(
        request,
        'landing/index.html',
        {
            'form': form,
            'waitlist_form': waitlist_form,
            'feedbacks': feedbacks,
        },
    )
