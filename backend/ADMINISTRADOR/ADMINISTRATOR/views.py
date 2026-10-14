from django.shortcuts import render

#Render for an ADMINISTRATOR/ request
def ADMINISTRATOR (request):
 return render(request, 'ADMINISTRATOR/index.html')
# Create your views here.
