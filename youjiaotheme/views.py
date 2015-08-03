from django.shortcuts import render


# Create your views here.

def youjiao(request):
    template_name = 'base.html'
    return render(request, template_name)
