from django.views.generic import DetailView, TemplateView
from star_ratings.models import Rating

from .models import Beer, Snack


class BeerRateView(TemplateView):
    model = Beer
    template_name = 'minimal_rating_system/article_ratings.html'

    def get_context_data(self, **kwargs):
        kwargs['article_class'] = "Beer"
        kwargs['articles'] = self.model.objects.all().order_by('date_created')
        return super(BeerRateView, self).get_context_data(**kwargs)


class SnackRateView(TemplateView):
    model = Snack
    template_name = 'minimal_rating_system/article_ratings.html'

    def get_context_data(self, **kwargs):
        kwargs['article_class'] = "Snack"
        kwargs['articles'] = self.model.objects.all().order_by('date_created')
        return super(SnackRateView, self).get_context_data(**kwargs)
