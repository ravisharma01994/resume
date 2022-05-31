from django.shortcuts import render

# Create your views here.
def home(request):
    context={'home':'active',
                'my':'My Resume'}
    return render(request,'core/home.html',context)

def contacts(request):
    context={'con':'active',
                'my':'Contact Me'}
    return render(request, 'core/contact.html',context)