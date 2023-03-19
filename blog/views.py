from django.shortcuts import render

from .models import Post

#from info import posts

# This code to connecting with html page


# posts = [
#     {
#         'author': 'Sam',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Mohammed',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     },
#     {
#         'author': 'Kaled',
#         'title': 'Blog Post 31',
#         'content': 'Thierd post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]



def home(request):
    context = {
        'posts': Post.objects.all()
        #'posts': posts  This code to make dataa come for the tope
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def dolf(request):
    return render(request,'blog/dolf.html', {'title': 'Dolf'})
