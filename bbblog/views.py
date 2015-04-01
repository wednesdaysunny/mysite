from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
# Create your views here.

def home_page(request):
    return HttpResponse("this is home page")

def hello(request):
    return HttpResponse("hell oworld")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('bbblog/current_datetime.html', {'current_date': now})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    print request
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        return HttpResponse('<table>%s</table>' % '\n'.join(html))