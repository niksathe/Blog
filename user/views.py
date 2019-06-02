from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.decorators import admin_required
from django.contrib.auth.models import User
from post.forms import PostForm
from post.models import Post, Comment
from django.shortcuts import get_object_or_404, Http404
from django.views.generic import ListView, DetailView


@login_required
def index(request):
        instance = request.user
        if instance.is_staff == True or instance.is_superuser == True:
                users = User.objects.all()
                posts_lists = Post.objects.all().order_by('id').reverse()
                paginator = Paginator(posts_lists, 1)  # Show 25 contacts per page
                page = request.GET.get('page')
                posts = paginator.get_page(page)

                context = {
                    'users' : users,
                    'posts' : posts,
                }
                return render(request, 'user/index.html', context)
        else:
            messages.warning(request, f'You are not authorized to acess this page!')
            return redirect('home')


'''def postss(request):
    keyword = request.GET.get("keyword")

    if keyword:
        posts = Post.objects.filter(title__contains = keyword)
        return render(request,"posts.html",{"posts":posts})
    posts = Post.objects.all()

    return render(request,"user/posts.html",{"posts":posts})'''





@login_required
def posts(request):
        instance = request.user
        if instance.is_staff == True or instance.is_superuser == True:
                posts_lists = Post.objects.all().order_by('id').reverse()
                paginator = Paginator(posts_lists, 10)  # Show 25 contacts per page
                page = request.GET.get('page')
                posts = paginator.get_page(page)

                context = {
                    'posts' : posts,
                }
                return render(request, 'user/posts.html', context)
        else:
            messages.warning(request, f'You are not authorized to acess this page!')
            return redirect('home')

@login_required
@admin_required
def users_list(request):
    object_list = User.objects.all()
    return render(request, 'user/users_list.html', {'users': object_list})


@login_required
@admin_required
def create_post(request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been created")
            return redirect("index")

        context = {
                'post_form': form,
        }

        return render(request, 'user/create_post.html', context)


@login_required
@admin_required
def edit_post(request, post_id=None):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect("index")

        context = {
                'post_form': form,
        }

        return render(request, 'user/edit_post.html', context)


def post_details(request, post_id=None):
        post = get_object_or_404(Post, id=post_id)
        comment_list = Comment.objects.filter(post=post_id).order_by('created_on').reverse()
        paginator = Paginator(comment_list, 5)  # Show 25 contacts per page
        page = request.GET.get('page')
        comment = paginator.get_page(page)
        context = {
            'post': post,
            'comments': comment,
        }




        return render(request, 'user/post_details.html', context)


class PostDetailSlugView(DetailView):
    queryset = Post.objects.all()
    template_name = "user/post_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("Not found..")
        except Post.MultipleObjectsReturned:
            qs = Post.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


@login_required()
def delete_post(request, post_id):
    post = get_object_or_404(Post,id = post_id)
    post.published = False
    post.save()
    messages.success(request,"Post Deleted")
    return redirect('posts')


def add_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
            user = request.POST['name']
            name = request.POST['name']
            email = request.POST['email']
            text = request.POST['text']
            newComment = Comment(user=user, name=name, email=email, text=text, post=post)
            newComment.post = post
            newComment.save()

    messages.success(request, 'Comment added')
    return redirect(reverse('post_details', kwargs={"post_id": post_id}))



@login_required
@admin_required
def create_subscription(request):
    return render(request, 'user/users_list.html', {})

@admin_required
@login_required
def add_to_fetured(request, post_id):
    post = get_object_or_404(Post,id = post_id)
    post.fetured = True
    post.save()
    messages.success(request,"Post added to featured list")
    return redirect('posts')

@admin_required
@login_required
def remove_from_fetured(request, post_id):
    post = get_object_or_404(Post,id = post_id)
    post.fetured = False
    post.save()
    messages.success(request,"Post added to featured list")
    return redirect('posts')




