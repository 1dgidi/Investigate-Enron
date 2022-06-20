from django.shortcuts import redirect, render
from django import forms
from django.forms import ModelForm, Textarea
from django.shortcuts import get_list_or_404, get_object_or_404
# from django.db.models import Count
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import EmailBody, PredictModel

import random
import re

class EForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EForm, self).__init__(*args, **kwargs)
        self.fields['body_text'].required = False
    class Meta:
        model = PredictModel
        fields = ['body_text']


def home(request):
    # print(list(request.POST.keys()))
    if request.method=='POST' and 'autofill' not in list(request.POST.keys()):
        form = EForm(request.POST)
        if form.is_valid():
            email_body = form.cleaned_data['body_text']
            new_req = PredictModel(body_text=email_body)
            new_req.save()
            print(reverse("bend:result", args=(new_req.id,)))
            return HttpResponseRedirect(reverse("bend:result", args=(new_req.id,)))
    elif 'autofill' in list(request.POST.keys()):
        primary_key = random.randint(1, EmailBody.objects.count())
        autofill_text = get_object_or_404(EmailBody, id=primary_key)
        context = {
            'form': EForm(initial={'body_text': autofill_text.body_text}),
        }
        return render(request, 'bend/home.html', context)
    return render(request, 'bend/home.html', {'form': EForm()})


def about(request):
    pass

def contact(request):
    pass

def result(request, pk):
    email = get_object_or_404(PredictModel, id=pk)
    count = len(email.body_text) if len(email.body_text) < 1000 else 1000
    context = {
        'email': ''.join(email.body_text[i] for i in range(count)),
        'author': email.who_wrote_it,
        'relation': email.relation
    }
    return render(request, 'bend/result.html', context)

# def autofill(request):
#     primary_key = random.randint(1, EmailBody.objects.count())
#     autofill_text = get_object_or_404(EmailBody, id=primary_key)

#     return redirect(
#         reverse('bend:home', 
#         kwargs={'form': EForm(initial={'body_text': autofill_text.body_text})}))



