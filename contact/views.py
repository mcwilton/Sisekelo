from django.shortcuts import render
from .forms import ContactForm, EnquiryForm

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def enquiry(request):
    form = EnquiryForm()
    return render(request, 'courses/course_detail.html', {'form': form})