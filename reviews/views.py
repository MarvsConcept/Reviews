from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        
        return render(request, "reviews/review.html", {
        "form":form
    })
        
    def post(self, request):
        form = ReviewForm(request.POST,)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        
        return render(request, "reviews/review.html", {
        "form":form
    })
    

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
    
    else:
        form = ReviewForm()
    
    return render(request, "reviews/review.html", {
        "form":form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html", {
        "has_error":False
    })