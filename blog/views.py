from django.shortcuts import render
#from info import posts

# This code to connecting with html page


posts = [
    {
        'name': 'Sam',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'name': 'Mohammed',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]



def home(request):
    contx = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', contx) # tocontact with html code.


def about(request):
   name = {'name': 'Fadhel'}
   return render(request, 'blog/about.html', {'title':'About'})


# # Create your views here.