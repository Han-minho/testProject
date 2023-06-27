from django.views.generic import TemplateView


class HomeView(TemplateView):
    tempate_name = 'home.html'