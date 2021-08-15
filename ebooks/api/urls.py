from django.urls import path, include

from ebooks.api.genericListCreateView import EbookListCreateAPIView, EbookGenericMixinListCreateAPIView
from rest_framework import routers
from ebooks.api.apiViewSet import EbookViewsets

router= routers.DefaultRouter()
router.register('books', EbookViewsets)

urlpatterns =[
    path('',include(router.urls)),
    path('ebooks-generic/',EbookGenericMixinListCreateAPIView.as_view(), name="ebooks_generics"),
]