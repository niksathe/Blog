from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator
from django.views.generic import DetailView


def working(request):
        return render(request, 'site/working.html', {})

def about(request):
        return render(request, 'site/about.html', {})

def terms_and_conditions(request):
        return render(request, 'site/terms.html', {})




def index(request):
        posts_lists = Post.objects.all().filter(fetured=1).reverse()
        paginator = Paginator(posts_lists, 3)
        page = request.GET.get('page')
        post = paginator.get_page(page)
        recent = Post.objects.all().order_by('id').reverse()
        paginator = Paginator(recent, 3)
        recent_page = request.GET.get('recent_page')
        recent_post = paginator.get_page(recent_page)
        context = {
                'post' : post,
                'recent_post' : recent_post,

        }
        return render(request, 'site/index.html', context)


def blog(request):
        posts_lists = Post.objects.all().order_by('id')
        paginator = Paginator(posts_lists, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context = {
                'posts' : posts,
        }
        return render(request, 'site/blog.html', context)

def most_recent(request):
        posts_lists = Post.objects.all().order_by('id').reverse()
        paginator = Paginator(posts_lists, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context = {
                'posts' : posts,
        }
        return render(request, 'site/most_recent.html', context)

class PostDetailSlugView(DetailView):
    queryset = Post.objects.all()
    template_name = "site/post_details.html"

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

