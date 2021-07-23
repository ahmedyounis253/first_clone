from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import CreateView
from . import models
from . import forms
class createpost(LoginRequiredMixin,CreateView):

    form_class=forms.PostForm
    template_name='main.html'
    model=models.Post



