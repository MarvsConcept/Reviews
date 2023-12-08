from django import forms 

class ReviewForm(forms.Form):
    User_Name = forms.CharField()