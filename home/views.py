from django.shortcuts import render

# Create your views here.


def index(request):
    template_data = {}
    template_data['title']="Movie_Store"
    return render(request, 'home/index.html', {'template_data':template_data})
def about(request):
    return render(request, 'home/about.html', {'template_data':{'title':"About"}})