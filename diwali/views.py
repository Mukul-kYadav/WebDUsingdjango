from django.shortcuts import render
import datetime 

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "diwali/index.html", {
        "diwali": now.month == 10 and now.day == 6
    })