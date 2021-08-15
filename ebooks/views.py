
from django.shortcuts import render
from django.urls import reverse_lazy
from ebooks.models import Ebook 
from django.views.generic import (TemplateView, ListView,
                                  DetailView, UpdateView,
                                  CreateView, DeleteView)
# template files is stored in templates folder under the app folder or on the root templates (after settings.py have been updated)
# EbookListView template name is Ebook_list.html - context =object_list 
# EbookDetailView template name is Ebook_detail.html - context =object
# EbookCreateView and EbookUpdateView template_name is Ebook_form.html - context = form
# EbookDeleteView is Ebook_confirm_delete.html - context=object

class EbookListView(ListView):
    #queryset=Ebook.objects.order_by('-pk')
    #context_object_name="Ebooks"
    model= Ebook
    #paginate_by=10
 
class EbookDetailView(DetailView):
    model=Ebook

class EbookCreateView(CreateView):
    model = Ebook
    fields=('__all__')

class EbookUpdateView(UpdateView):
    model = Ebook
    fields=('__all__')

class EbookDeleteView(DeleteView):
    model = Ebook
    success_url=reverse_lazy("ebook:list")
