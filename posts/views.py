from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.conf import settings
import os
from productapp.models import Chapter, Brand, Category, Department, Product

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
    product_list = []
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
            my_brand = Brand.objects.get(name=my_list[4])
            my_category = Category.objects.get(name=my_list[5])
            my_department = Department.objects.get(name=my_list[6])
            my_chapter = Chapter.objects.get(name=my_list[7])
            Product.objects.create(style=my_list[0], name=my_list[1], color=my_list[2],
                                   color_name=my_list[3], brand=my_brand, category=my_category,
                                   department=my_department, chapter=my_chapter,
                                   image_link=my_list[8], description=my_list[9])
            product_list.append(my_list[0])
    content = {
        'file_name': file.cover,
        'product_list': product_list,
    }
    return render(request, 'posts/ok.html', content)


