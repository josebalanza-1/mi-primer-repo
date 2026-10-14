from django.http import HttpResponse
from django.shortcuts import render

#Make a homepage request for petition, index on templates
def homepage(request):
    return render(request, 'index.html')