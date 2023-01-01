from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import News
from .forms import News_Create_Form
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

class News_List(ListView):
    queryset = News.objects.all()
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    

class News_Details(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'info'


class News_Create(CreateView):
    model = News
    form_class = News_Create_Form
    template_name = 'news/news_detail.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)