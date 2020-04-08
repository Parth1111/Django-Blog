from django.shortcuts import render

# Create your views here.

#dummy data to pass to templates
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'August 27 2018'
    },
    {
        'author': 'ANC Jacob',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'September 12 2018'
    },
    {
        'author': 'Joe Exotic',
        'title': 'Blog Post 3',
        'content': 'Third post',
        'date_posted': 'December 02 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')