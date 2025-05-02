from django.urls import path
from .views import RecipeListView, RecipeSearchView
from . import views

urlpatterns = [
 path('ui/', views.recipe_ui, name='recipe-ui'),
 path('recipes/', RecipeListView.as_view(), name='recipe-list'),
 path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
]
