from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.filters import BaseFilterBackend, OrderingFilter
from rest_framework import permissions
from helpers.views import StatusOnly200Mixin
from .serializers import *


class CategoryFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category_id = request.query_params.get('category', None)
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                return queryset.empty()
            else:
                return queryset.filter(category=category)
        else:
            return queryset


class ProductListView(StatusOnly200Mixin, ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    filter_backends = (CategoryFilter, )
    queryset = Product.objects.all()
    serializer_class = ShortProductSerializer


class ProductView(StatusOnly200Mixin, RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer


class CategoriesListView(StatusOnly200Mixin, ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CategorySerializer
