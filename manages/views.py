from django.shortcuts import render, render_to_response
from models import Good
# Create your views here.

def input_good(request):
    print "----------------"
    return render_to_response('manages/input_goods.html')

def submit_good(request):
    print "----------------1"
    print request.POST
    print "----------------2"
    if 'name' in request.POST:
        g = Good(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        g.save()

    gss = Good.objects.all()
    return render_to_response('manages/show_goods.html', {'goods': gss})