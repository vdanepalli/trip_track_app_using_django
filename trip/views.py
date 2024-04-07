from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Trip, Note

class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trips_list(request):
    # print(dir(request))
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips
    }
    return render(request, 'trip/trip_list.html', context)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"] # what fields to include
    # looks for template named model_form.html

    def form_valid(self, form): # we are overriding this 
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TripDetailView(DetailView):
    model = Trip # with this alone, we only get the Trip data but not the notes data.

    def get_context_data(self, **kwargs): # we override this to get the Note data as well
        context = super().get_context_data(**kwargs)
        trip = context['object'] 
        notes = trip.notes.all()
        context['notes'] = notes
        return context

class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"]
    #template named model_form.html

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')

class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

    # update uses the same template as the create note_form.html
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    #not make the template - send post requests here
    # no template needed, send a post request to this url 
    
    