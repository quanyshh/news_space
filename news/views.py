from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateResponseMixin,View
from django.views.generic import DetailView,ListView
from .models import Post, Comment,Category
from news_and_video.models import Video
from .forms import CommentForm
from django.views import View
from django.http import Http404
from django.db.models import Count


class HomeView(TemplateResponseMixin,View):
    template_name = 'index.html'
    def get(self,request):
        categorys = Category.objects.all();
        videos = Video.objects.all();
        category_post_counts = Category.objects.annotate(post_count=Count('post'))
        posts = Post.objects.all()
        return self.render_to_response({'videos':videos,'categorys': categorys, 'posts':posts,'category_post_counts':category_post_counts})


class AboutView(TemplateResponseMixin,View):
    template_name = 'about.html'
    def get(self,request):
        contact = ''
        return self.render_to_response({'contact':contact})


class PostDetailView(TemplateResponseMixin, View):
    template_name = 'post/post_detail.html'

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        categorys = Category.objects.all();
        category_post_counts = Category.objects.annotate(post_count=Count('post'))
        post.views += 1
        post.save()
        comments = Comment.objects.filter(post=post)
        comment_count = comments.count() 
        comment_form = CommentForm()
        return self.render_to_response({'categorys':categorys,'post': post, 'id': id, 'comment_form': comment_form, 'comments': comments,'comment_count':comment_count,'category_post_counts':category_post_counts})

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        categorys = Category.objects.all();
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            obj_save = comment_form.save(commit=False)
            obj_save.user = request.user
            obj_save.post = post
            obj_save.save()
            return redirect('news:post_detail', id=id)
        return self.render_to_response({'categorys':categorys,'post': post, 'id': id, 'comment_form': comment_form, 'comments': comments,'comment_count':comment_count,'category_post_counts':category_post_counts})

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)