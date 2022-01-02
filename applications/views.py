from django.shortcuts import render
from .forms import ApplicationForm


# def post_new(request):
#     form = ApplicationForm()
#     return render(request, ', {'form': form})'


def post_new(request):
    form = ApplicationForm()
    return render(request, 'application/application.html', {'form': form})

 #
# def application(request):
# 	context = {
# 		"hello" = "hello"
# 	}
# 	render (request, "application/application.html" context )