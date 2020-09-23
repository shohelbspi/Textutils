# I have created this file - Shohel

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'remove punctuations','Analyzed_Text': analyzed}
        djtext = analyzed

    if(uppercase=='on'):
        analyzed =''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to your text upper case', 'Analyzed_Text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'NewLines Remover', 'Analyzed_Text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'Analyzed_Text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = djtext
        analyzed = len(analyzed)
        params = {'purpose': 'Text Char Count ', 'Analyzed_Text': analyzed}
        return render(request, 'analyze.html', params)

    if (removepunc != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover  != "on" and charcount != 'on' ):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')