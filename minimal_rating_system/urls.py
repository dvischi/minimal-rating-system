from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from minimal_rating_system.views import BeerRateView, SnackRateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='minimal_rating_system/home.html'), name="home"),
    url(r'^beer_ratings$', BeerRateView.as_view(), name='beer_ratings'),
    url(r'^snack_ratings$', SnackRateView.as_view(), name='snack_ratings'),
]
