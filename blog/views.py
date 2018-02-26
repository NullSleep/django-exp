from django.shortcuts import render

# Create your views here.

#A view is a place where we put the "logic" of our application.

def lista_posts(request):
    return render(request, 'blog/lista_posts.html', {})
