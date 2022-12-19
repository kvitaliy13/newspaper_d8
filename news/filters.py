import django
import django_filters
from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    date_time__gt = django_filters.DateFilter(
        field_name="time_in_post", label="Поиск по дате", lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))

    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'post_text': ['icontains'],
           'time_in_post': ['gte',],
       }