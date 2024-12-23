import django_filters


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "price": ["lt", "gt"],
            "category": ["exact"],
            "condition": ["exact"],
            "created_at": ["lt", "gt"],
        }
