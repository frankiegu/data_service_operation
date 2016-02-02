#A validator is a callable that takes a value and raises a 
#ValidationError if it doesn¡¯t meet some criteria. Validators can be useful 
#for re-using validation logic between different types of fields.
#For example, here¡¯s a validator that only allows even numbers:

from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)

#You can add this to a model field via the field¡¯s validators argument:
from django.db import models
class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])

#Because values are converted to Python before validators are run, you can 
#even use the same validator with forms:
from django import forms
class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])