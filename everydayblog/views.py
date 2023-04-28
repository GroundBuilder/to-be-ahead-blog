from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='p').order_by('created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='p')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comment.filter(approved=True).order_by('-created_on')
        liked = False

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            },
        )
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='p')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')


        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
            },
        )
    


# class PostListPublic(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status='o').order_by('created_on')
#     template_name = 'public.html'
#     paginate_by = 3