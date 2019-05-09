from django import forms
from .categories import categories
class ProductInputForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    publisher = forms.CharField()
    category = forms.ChoiceField(choices=categories)
    price = forms.IntegerField()
    photo = forms.ImageField()
    units = forms.IntegerField()
    pages = forms.IntegerField()
    publish_year = forms.CharField(max_length=4)
    details = forms.CharField(widget = forms.Textarea)
    tags = forms.CharField()
    is_bestseller = forms.BooleanField(required=False)
    is_award_winner = forms.BooleanField(required=False)