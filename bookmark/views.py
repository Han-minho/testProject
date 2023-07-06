from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView, TemplateView, FormView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin
from bookmark.models import Bookmark


# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    pass


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    pass


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    pass


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    pass
