from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# # Create your views here.


class SchoolListView(ListView):
    # Notes order: From bottom to the top
    ### IMPORTANT ###
    # This(context_object_name) however sets the name of the returned value to our custom choice.
    ###   #####   ###
    context_object_name = 'schools'
    ### IMPORTANT ###
    # this(model) returns: school_list casue the "ListView" brings the model name to lower case and adds : "_list"!
    ### #### ###
    model = models.School


class SchoolDetailView(DetailView):
    ### IMPORTANT ###
    # Same here with "DetailView". Our model when called will returned model object lower cased.
    context_object_name = 'school_details'
    model = models.School
    template_name = 'CBVs_app/school_details.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("CBVs_app:list")
# Not a cbv
# def index(request):
#     return render(request, 'CBVs_app/index.html')


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = 'CBVs_app/index.html'
