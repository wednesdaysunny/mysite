from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from form import ContactForm
import datetime


def search_form(request):
    return render_to_response('books/search_form.html')


def search(request):
    print request.GET
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'

    return HttpResponse(message)

def thanks(request):
    now = datetime.datetime.now()
    return render_to_response('bbblog/current_datetime.html', {'current_date': now})

def contact(request):
    errors = []
    print("11111")
    if request.method == 'POST':
        print("2222")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("3333")
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'), ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
        else:
            print("4444")
            return render_to_response('books/contact_form.html', {'form': form})
    else:
        print("55555")
        form = ContactForm(initial={'subject': 'I love your site!'})
        return render_to_response('books/contact_form.html', {'form': form})