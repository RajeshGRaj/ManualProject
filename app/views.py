from email import message
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    topics = Topics.objects.all()
    return render(request, 'index.html', {'topics':topics})

def topic_details(request, id):
    try:
        what = Whats.objects.filter(id=id)
        when = Whens.objects.filter(id=id)
        why = Whys.objects.filter(id=id)
        how = Hows.objects.filter(id=id)
        types = Typses.objects.filter(id=id)
    except:
        mes = ""
    return render(request, 'content.html', {'what':what, 'when':when, 'why':why, 'how':how, 'types':types})

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You for Your Feedback!')   
            return redirect("/feedback")
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form':form})