from django.shortcuts import render

def default(request):
    return render(request, "google/index.html")

def advanced(request):
    return render(request, "google/advanced.html")
    
def images(request):
    return render(request, "google/images.html")
