from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import Category, Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count
from django.db.models import Q

# Create your views here.

class Post_List(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/blog_list.html'
    paginate_by = 5
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super(Post_List, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['lastest_post'] = self.queryset[:1]
        context['popular_post'] = Post.objects.order_by('-hit_count_generic__hits')[:4]
        return context
    
    
def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    post_tags = post.tags.all()

    form = Comment_Form()
    if request.method == "POST":
        form = Comment_Form(request.POST)
        if form.is_valid():
            comment = Comment(**form.cleaned_data,post=post)
            comment.save()
    comments = Comment.objects.filter(post=post)
    similar_posts = Post.published.filter(tags__in=post_tags).exclude(pk=pk)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags')[:6]

    context = {
		"post" : post,
        "similar_posts" : similar_posts,
		"comments" : comments,
		"form" : form,
	}
    print(" My Similar Post is ",similar_posts)
    return render(request,'blog/blog_detail.html',context)

'''

class Post_Details(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'info'

'''
class Post_Create(CreateView):
    model = Post
    form_class = Post_Create_Form
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class Category_List(ListView):
    queryset = Category.objects.all()
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super(Category_List, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(categories__name=self.kwargs['category'])
        print(context)
        return context

class Search_Page(ListView):
    template_name = 'blog/blog_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query)| Q(body__icontains=query))
        return object_list
    
    