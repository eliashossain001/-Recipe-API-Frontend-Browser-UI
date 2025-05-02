from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render  # ✅ For your frontend UI page

from .models import Recipe
from .serializers import RecipeSerializer
from .pagination import CustomPagination

# ----------------------------- 
# Frontend UI View (renders index.html)
# -----------------------------
def recipe_ui(request):
    return render(request, 'recipes/index.html')

# ----------------------------- 
# Recipe List View (With Pagination)
# -----------------------------
class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination

    # Search by title (partial match)
    search_fields = ['title']

    # Filter by cuisine, total_time, rating
    filterset_fields = ['cuisine', 'total_time', 'rating']

    # Order by rating (default DESC)
    ordering_fields = ['rating']
    ordering = ['-rating']

# ----------------------------- 
# Recipe Search View (Advanced Filters - Calories, etc)
# -----------------------------
class RecipeSearchView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = None  # No pagination

    def get_queryset(self):
        queryset = super().get_queryset()

        # Calories filtering
        calories = self.request.query_params.get('calories', None)
        if calories:
            calories_operator = calories[:2] if calories[1] in "=<>!" else calories[0]
            calories_value = calories.lstrip("<=!>")
            if calories_operator == "<=":
                queryset = queryset.extra(where=["CAST(json_extract(nutrients, '$.calories') AS INTEGER) <= %s"], params=[calories_value])
            elif calories_operator == ">=":
                queryset = queryset.extra(where=["CAST(json_extract(nutrients, '$.calories') AS INTEGER) >= %s"], params=[calories_value])
            elif calories_operator == "<":
                queryset = queryset.extra(where=["CAST(json_extract(nutrients, '$.calories') AS INTEGER) < %s"], params=[calories_value])
            elif calories_operator == ">":
                queryset = queryset.extra(where=["CAST(json_extract(nutrients, '$.calories') AS INTEGER) > %s"], params=[calories_value])
            elif calories_operator == "=":
                queryset = queryset.extra(where=["CAST(json_extract(nutrients, '$.calories') AS INTEGER) = %s"], params=[calories_value])

        # Rating filtering
        rating = self.request.query_params.get('rating', None)
        if rating:
            rating_operator = rating[:2] if rating[1] in "=<>!" else rating[0]
            rating_value = rating.lstrip("<=!>")
            if rating_operator == "<=":
                queryset = queryset.filter(rating__lte=rating_value)
            elif rating_operator == ">=":
                queryset = queryset.filter(rating__gte=rating_value)
            elif rating_operator == "<":
                queryset = queryset.filter(rating__lt=rating_value)
            elif rating_operator == ">":
                queryset = queryset.filter(rating__gt=rating_value)
            elif rating_operator == "=":
                queryset = queryset.filter(rating=rating_value)

        # Title
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Cuisine
        cuisine = self.request.query_params.get('cuisine', None)
        if cuisine:
            queryset = queryset.filter(cuisine=cuisine)

        # Total time
        total_time = self.request.query_params.get('total_time', None)
        if total_time:
            queryset = queryset.filter(total_time=total_time)

        return queryset

    # Custom list response
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "data": serializer.data
        })
