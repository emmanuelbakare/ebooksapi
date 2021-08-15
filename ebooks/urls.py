from django.urls import path
from ebooks import views


app_name="ebook"
urlpatterns = [
    path('', views.EbookListView.as_view(), name="list"),
    path('<int:pk>/', views.EbookDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', views.EbookUpdateView.as_view(), name="updated"),
]
