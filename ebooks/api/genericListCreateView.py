from  rest_framework import generics
from rest_framework import  mixins

from ebooks.models import Ebook
from ebooks.api.serializer import EbookSerializer, ReviewSerializer


class EbookGenericMixinListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# you can use the one above or below 

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class=EbookSerializer

class EbookListCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class=EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class=EbookSerializer

    def perform_create(self, serializer):
        bookid=self.kwargs.get('pk')
        book= Ebook.objects.get(id=bookid)
        serializer.save(book=book)
