from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie, Review 

from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else :
        movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'template_data':{"title":"movies","movies":movies}})

def show(request, id):
    movie = Movie.objects.get(id=id)
    review = Review.objects.filter(movie=movie)
    return render(request, 'movies/show.html',{'template_data':{"title":movie.name, "movie":movie, 'reviews':review}})
@login_required
def create_review(request, id):
    if request.method=='POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        rev =  Review()
        rev.comment = request.POST['comment']
        rev.movie = movie
        rev.user = request.user
        rev.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('movies.show', id=id)
        