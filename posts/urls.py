from django.urls import path

from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView  #, list_all_posts, show_post_detail

urlpatterns = [
    # path("<int:pk>/", show_post_detail, name="post_detail"),  # here is where pk is grabbed as an int
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),  # must use .as_view() method
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),  # want to update a specifc view
]
