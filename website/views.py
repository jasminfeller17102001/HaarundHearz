from django.shortcuts import render


def index(request):
    """Homepage View"""
    return render(request, 'website/index.html')
