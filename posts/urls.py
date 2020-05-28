from django.urls import path

from .views import PostPageView, load_file_view

urlpatterns = [
    path('', PostPageView.as_view(), name='posts'),
    path('load_file/<int:pk>/', load_file_view, name='load_file'),
]

# import posts.views as posts
#
# app_name = 'posts'
#
# urlpatterns = [
#     path('', posts.posts_view, name='posts'),
# ]
