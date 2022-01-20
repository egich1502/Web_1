from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='имя клиента', min_length=3, widget=forms.TextInput(attrs={'class': 'myfield'}))
    age = forms.IntegerField(label='возраст клиента', min_value=1, max_value=100,
                             widget=forms.NumberInput(attrs={'class': 'myfield'}))
    required_css_class = 'field'
    error_css_class = 'error'
