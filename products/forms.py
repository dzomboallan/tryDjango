from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":'Your title'}))
    description = forms.CharField (required=False, widget=forms.Textarea(attrs={'class':'new-class-name two',
                                                                                 'id':'my-id-for-textarea',
                                                                                 'row':20,
                                                                                 'cols':120
                                                                                 }))
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_titles(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE"  in title:
            forms.ValidationError('This is not a valid title')
        return title
            


class RawForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":'Your title'}))
    description = forms.CharField (required=False, widget=forms.Textarea(attrs={'class':'new-class-name two',
                                                                                 'id':'my-id-for-textarea',
                                                                                 'row':20,
                                                                                 'cols':120
                                                                                 }))
    price = forms.DecimalField(initial=199.99)