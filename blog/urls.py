from django.urls import path

from .views import BlogListView, BLogDetailsView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BLogDetailsView.as_view(), name="post_detail"),
]
