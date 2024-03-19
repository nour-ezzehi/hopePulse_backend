from django.urls import path
from django.views.generic import TemplateView

app_name = 'campaign'

urlpatterns = [
  path('', TemplateView.as_view(template_name='campaign/index.html'))
]
