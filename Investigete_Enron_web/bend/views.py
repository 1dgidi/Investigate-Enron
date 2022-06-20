from django.shortcuts import redirect, render
from django import forms
from django.forms import ModelForm, Textarea
from django.shortcuts import get_list_or_404, get_object_or_404
# from django.db.models import Count
from django.urls import reverse

from .models import EmailBody, PredictModel

import random
import re

class EForm(ModelForm):
    class Meta:
        model = PredictModel
        fields = ['body_text']


def home(request):
    if request.method=='POST':
        form = EForm(request.POST)
        if form.is_valid():
            email_body = form.cleaned_data['body_text']
            new_req = PredictModel(body_text=email_body)
            new_req.save()
            return redirect('bend:result', new_req.id)
    return render(request, 'bend/home.html', {'form': EForm()})


def about(request):
    pass

def contact(request):
    pass

def result(request, pk):
    email = get_object_or_404(PredictModel, id=pk)
    context = {
        'email': email.body_text[:50],
        'author': email.who_wrote_it,
        'relation': email.relation
    }
    return render(request, 'bend/result.html', context)

def autofill(request):
    primary_key = random.randint(1, EmailBody.objects.count())
    autofill_text = get_object_or_404(EmailBody, id=primary_key)

    return redirect(
        reverse('bend:home', 
        kwargs={'form': EForm(initial={'body_text': autofill_text.body_text})}))



