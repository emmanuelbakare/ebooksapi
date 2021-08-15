    from  rest_framework import viewsets

    from ebooks.models import Ebook
    from ebooks.api.serializer import EbookSerializer



    class EbookViewsets(viewsets.ModelViewSet):
        
        queryset= Ebook.objects.all()
        serializer_class = EbookSerializer
