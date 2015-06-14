from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views import generic
from adverts.models import Advert


class IndexView(generic.ListView):
    template_name = 'adverts/index.html'
    context_object_name = 'latest_advert_list'

    def get_queryset(self):
        """
        :return: The last five published adverts.
        """
        return Advert.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
    model = Advert
    template_name = 'adverts/detail.html'