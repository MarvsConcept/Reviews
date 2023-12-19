from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(CreateView):
    model = Review
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank_you"
    
    
# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/thank_you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
        
#         return render(request, "reviews/review.html", {
#         "form":form
#     })
        
#     def post(self, request):
#         form = ReviewForm(request.POST,)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank_you")
        
#         return render(request, "reviews/review.html", {
#         "form":form
#     })
    

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST,)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank_you")
    
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {
#         "form":form
#     })

class thank_youView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context         

# def thank_you(request):
#     return render(request, "reviews/thank_you.html", {
#         "has_error":False
#     })

# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" 
    
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id ==  str(loaded_review.id)
        return context
        
# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)