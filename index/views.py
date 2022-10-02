from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request, html='index'):
    try:
        return render(request, f"{html}.html")
    except:
        return render(request, f"index.html")


def form(request):
    return render(request, 'form.html')