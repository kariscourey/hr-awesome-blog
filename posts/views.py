from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

try:
    from posts.models import Post
except Exception:
    Post = None


# Loads a page for one object
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    # context_object_name  # not necessary because default is lowercase model name


# # Create your views here.
# def show_post_detail(request, pk):  # pk is an int
#     # django points at id field, "primary key"
#     # to customize, customize in models like
#     # unique_id = models.BigAutoField(primary_key=True)
#     if Post:
#         post = Post.objects.get(pk=pk)
#     else:
#         post = None
#     context = {
#         "post": post,
#     }
#     return render(request, "posts/detail.html", context)



# Loads a page for many objects

# creates a context automatically, and puts object_list as the list of
# objects it gets from the db, but it also puts "modelname_list"
# as the list of objects

# don't need to make a context dictionary, don't need to use render, no specified request
class PostListView(ListView):
    model = Post  # set model attribute to actual model
    template_name = "posts/list.html"  # set to path of template
    context_object_name = "posts"
    paginate_by = 10

    # using this to print and return context for debugging purposes
    # get context data could also be used to add stuff to the context
    # e.g. add custom keys
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self):  # want just the posts that match the query

        # get query the user typed via GET request
        query = self.request.GET.get("q")

        # use model to query db
        if not query:
            # query = ""
            return Post.objects.all()

        # return results of query
        return Post.objects.filter(title__icontains = query)
        # return Post.objects.filter(query)



# def list_all_posts(request):
#     # Calling the post model and fetching all the post objects from the db
#     # Returns a list of post objects
#     posts = Post.objects.all()
#     # Creates a context dictionary; all keys in context can be called in template
#     context = {
#         "posts": posts,
#     }
#     # Render a template; give request, string of path, and context dict
#     return render(request, "posts/list.html", context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/create.html'
    success_url = "/"


class PostUpdateView(UpdateView):
    model = Post  # model the data is coming from
    fields = ['title', 'content']
    template_name = 'posts/update.html'
    success_url = "/"
