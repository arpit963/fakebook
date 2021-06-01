import django_filters
from django_filters import CharFilter
from .models import Profile

class ProfileFilter(django_filters.FilterSet):
    user = CharFilter(field_name='first_name', lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = []