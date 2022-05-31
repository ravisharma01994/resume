from django.shortcuts import render

# Create your views here.
def service(request):
    context={'ser':'active',
                'my':'Services'}
    return render(request, 'serv/services.html',context)
    