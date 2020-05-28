from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.conf import settings
import os

from .models import Post

class PostPageView(ListView):
    model = Post
    template_name = 'posts/post.html'


# def posts_view(request):
#     post_list = Post.objects.all()
#     if request.method == 'POST':
#         print('loaded')
#         return render(request, 'posts/ok.html')
#     else:
#         content = {
#             'object_list': post_list
#         }
#
#         return render(request, 'posts/post.html', content)

def load_file_view(request, pk):
    file = get_object_or_404(Post, pk=pk)
    data_path = os.path.join(settings.MEDIA_ROOT, str(file.cover))
    data_file = open(data_path, "r", encoding='UTF-8')
    data = data_file.readlines()  # read ALL the lines!
    data_file.close()
    line_number = -1
    for item in data:
        line_number += 1
        if line_number > 0:
            my_list = item.replace('\n', '')
            my_list = my_list.split('\t')


    content = {
        'file_name': file.cover,
        'product': my_list,
    }
    return render(request, 'posts/ok.html', content)


