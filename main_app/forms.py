from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    class Meta:
      model = Feeding
      fields = ['date', 'meal']
      widgets = {
          'date': forms.DateInput(attrs={'type': 'text', 'class': 'datepicker', 'id': 'id_date'}),
      }
