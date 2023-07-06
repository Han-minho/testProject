from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from photo.models import Album, Photo
from mysite.views import OwnerOnlyMixin

# Create your views here.
class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


class PhotoCV(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ('album','title','image','description')
    succes_url = reverse_lazy('photo:index')


class PhotoChangeLV(LoginRequiredMixin,ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin,UpdateView):
    model = Photo
    success_url = reverse_lazy('photo:index')


class PhotoDelV(OwnerOnlyMixin,DetailView):
    model = Photo
    success_url = reverse_lazy('photo:index')


