
from django import forms


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    name = forms.CharField(label='search',
                           initial='your name',
                           widget=forms.Textarea(attrs={'rows': 30, 'cols': 100}))
