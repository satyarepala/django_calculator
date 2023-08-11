from django import forms
from .models import Feedback

class BasicCalculatorForm(forms.Form):
    num1 = forms.FloatField(label='Number 1', required=False)
    num2 = forms.FloatField(label='Number 2', required=False)
    operation = forms.ChoiceField(choices=[
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide')
    ], label='Operation')

class AdvancedCalculatorForm(forms.Form):
    num1 = forms.FloatField(label='Number 1', required=False)
    num2 = forms.FloatField(label='Number 2', required=False)
    operation = forms.ChoiceField(choices=[
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide'),
        ('square_root', 'Square Root'),
        ('exponent', 'Exponent')
    ], label='Operation')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text']



