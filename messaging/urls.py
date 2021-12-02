from django.urls import path, include
from django.views.generic import TemplateView


app_name = 'messaging'

urlpatterns = [
    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
]
