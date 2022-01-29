from django import forms

from .models import Contact, Enquiry


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'



class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

