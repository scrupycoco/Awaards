from django.shortcuts import render, redirect
from awardsposts . models import Post
from awardsposts.forms import RatingForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def home(request):
    post = Post.objects.all().order_by('-last_modified')

    context={
        'posts' : post,
    }
    return render(request, 'awardshome/home.html', context)

def about(request):
    return render(request, 'awardshome/about.html', {'title':'About'})

@csrf_protect
def rating(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = Ratings(
                author = request.user,
                post = post,
                design_rating = form.cleaned_data["design_rating"],
                usability_rating = form.cleaned_data["usability_rating"],
                content_rating = form.cleaned_data["content_rating"],
                comment = form.cleaned_data["comment"],
            )
            rating.save()

            return redirect('awards-home')

    else:
        form = RatingForm()


    context={
        'post' : post,
        'form' : form,
    }
    return render(request, 'awardshome/rating.html', context)
