from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(),),
    path('thank_you', views.thank_youView.as_view(),),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view()),
]