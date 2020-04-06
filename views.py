# I have created this file-Param
from typing import Dict

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'paramjit', 'place':'Canada'}
    return render(request, 'index.html',params)


def analyze(request):
    #get the text
    djtext= request.POST.get('text','default')
     # check checkbox value
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlinerem= request.POST.get('newlinerem','off')
    spaceremover= request.POST.get('spaceremover','off')
    print(removepunc)
    print(djtext)
     #check with checkbox is on
    if removepunc == "on":
     #analyzed = djtext
     punctuations = '''! ()-[] {}:;' "\,<>./?@#$%^&*_~'''
     analyzed=""
     for char in djtext:
         if char not in punctuations:
             analyzed= analyzed+char
     params = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
     djtext=analyzed
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newlinerem == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(spaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]== "  ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        # analyze the text
    if(removepunc !="on" and fullcaps !='on'and newlinerem != 'on' and spaceremover !='on' ):
        return HttpResponse(djtext)
    return render(request, 'analyze.html', params)
