from django.shortcuts import redirect, render
from django import forms
from django.forms import ModelForm, Textarea

from .models import EmailBody


class EForm(ModelForm):
    class Meta:
        model = EmailBody
        fields = ['body_text']


def home(request):
    if request.POST:
        form = EForm(request.POST)
        if form.is_valid():
            email_body = form.cleaned_data['body_text']
            new_req = EmailBody(body_text=email_body)
            new_req.save()
            return redirect('bend:result', new_req.id)
    return render(request, 'bend/home.html', {'form': EForm()})

def about(request):
    pass

def contact(request):
    pass

def result(request, pk):
    pass

