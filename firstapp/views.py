from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'firstapp/index.html', {})
    
def learnmore(request):
    return render(request, 'firstapp/learnmore.html')