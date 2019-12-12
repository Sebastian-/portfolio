from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
