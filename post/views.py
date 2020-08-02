from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def post_view(request):
    return render(request, 'blog.html')