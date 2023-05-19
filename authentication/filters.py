from .models import User
from django_filters import rest_framework as filters

# from django_filters.fields import Lookup
# from django_filters import Filter
from django.db.models import Q
from django.utils import timezone
import datetime


DATES = (
    ("today", "Today"),
    ("week", "This week"),
    ("month", "This month"),
    ("year", "This year"),
)


class UserFilter(filters.FilterSet):
    date = filters.ChoiceFilter(
        method="was_recent", choices=DATES, label="Created Time"
    )

    o = filters.OrderingFilter(
        fields=(
            ("date_joined", "date_joined"),
            ("username", "username"),
            ("id", "id"),
        ),
        field_labels={
            "date_joined": "Sort by date_joined",
            "username": "Sort by username",
            "id": "Sort by id",
        },
    )

    def was_recent(self, queryset, name, value):
        now = timezone.now()
        if value == "today":
            return queryset.filter(
                Q(date_joined__gt=now - datetime.timedelta(days=1))
                & Q(date_joined__lt=now)
            )
        elif value == "week":
            return queryset.filter(
                Q(date_joined__gt=now - datetime.timedelta(days=7))
                & Q(date_joined__lt=now)
            )
        elif value == "month":
            return queryset.filter(
                Q(date_joined__gt=now - datetime.timedelta(days=30))
                & Q(date_joined__lt=now)
            )
        elif value == "year":
            return queryset.filter(
                Q(date_joined__gt=now - datetime.timedelta(days=360))
                & Q(date_joined__lt=now)
            )
        else:
            return queryset

    class Meta:
        model = User
        fields = ["id", "username", "date_joined"]


# class FreelancersFilter(filters.FilterSet):

#     date = filters.ChoiceFilter(
#         method='was_recent', choices=DATES, label="Created Time")

#     o = filters.OrderingFilter(
#         fields=(
#             ('created', 'created'),

#         ),

#         field_labels={
#             'created': 'Sort by created time',
#         }
#     )

#     def was_recent(self, queryset, name, value):
#         now = timezone.now()
#         if value == "today":
#             return queryset.filter(Q(created__gt=now - datetime.timedelta(days=1)) & Q(created__lt=now))
#         elif value == "week":
#             return queryset.filter(Q(created__gt=now - datetime.timedelta(days=7)) & Q(created__lt=now))
#         elif value == "month":
#             return queryset.filter(Q(created__gt=now - datetime.timedelta(days=30)) & Q(created__lt=now))
#         elif value == "year":
#             return queryset.filter(Q(created__gt=now - datetime.timedelta(days=360)) & Q(created__lt=now))
#         else:
#             return queryset

#     class Meta:
#         model = FreelancerProfile
#         fields = ['profession', 'city', 'full_name']


# class BrandFilter(filters.FilterSet):

#     class Meta:
#         model = Brand
#         fields = ['category']


# class SearchingFilter(filters.FilterSet):
#     category_id = filters.NumberFilter(field_name="category__id", lookup_expr='exact')
#     name = filters.CharFilter(field_name="translations__name", lookup_expr="icontains")
#     new = filters.BooleanFilter(method='was_recent')

#     def was_recent(self, queryset, name, value):
#         now = timezone.now()
#         if value == True:
#             return queryset.filter(Q(created__gt=now - datetime.timedelta(days=7)) & Q(created__lt=now))
#         else:
#             return queryset

# class Meta:
#     model = Product
#     fields =['discount']


# For Dynamic Search
# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])


# TODO: COMMENT FILTER
# def departments(request):
#     if request is None:
#         return Department.objects.none()

#     company = request.user.company
#     return company.department_set.all()

# class EmployeeFilter(filters.FilterSet):
#     department = filters.ModelChoiceFilter(queryset=departments)


# FUNCTION FILTER
#  find_anywhere = filters.CharFilter(method='look_anywhere')
# def look_anywhere(self, queryset, name, value):
#     return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))


# with_discount = filters.BooleanFilter(method='get_discount')
# def get_discount(self, queryset, name, value):
#     return queryset.filter(discount )
# TODO: When postgres is linked open this
# def filter_search(self, queryset, name, value):
#     return queryset.annotate(search=SearchVector('name', 'description')).filter(search=value)

# search = filters.CharFilter(method='filter_search')
# category_ids = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), to_field_name='id', field_name='category__id')
# subcategory_id = filters.CharFilter(field_name="subcategory__id", lookup_expr='exact')

# o = filters.OrderingFilter(
#     # tuple-mapping retains order
#     fields=(
#         ('new_price', 'price'),
#         ('created', 'created')

#     ),

#     # labels do not need to retain order
#     field_labels={
#         'price': 'Sort price ',
#     }
# )
