from django.shortcuts import render

# Create your views here.
def skill(request):
    context={'skl':'active',
                'my':'My Skills'}
    return render(request, 'edu/skills.html',context)