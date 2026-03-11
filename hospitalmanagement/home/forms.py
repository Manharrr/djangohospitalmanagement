from django import forms

from .models import Booking

class Dateinput(forms.DateInput):
    input_type='date'

class BookingForms(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'bookingdate':Dateinput(),
        }
        label={
            'pname':"patient name:",
            'pphone':"patient phone",
            'eemail':"patient email",
            'docname':"doctor name",
            'bookingdate':"booking date"
        }
