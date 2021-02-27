from django import forms

from cities.models import City
from trains.models import Train



class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    cities = forms.ModelMultipleChoiceField(label='Through the cities', queryset=City.objects.all(),
                                            required=False, widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }))

    traveling_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time',
    }))


    class Meta:
        model = Train
        fields = '__all__'