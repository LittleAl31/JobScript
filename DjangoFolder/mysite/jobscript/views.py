from django.shortcuts import render

from django.http import HttpResponse

from .JobScript import *

from .models import InputForm

# Create your views here.


myJS = JobScriptAnalyzer()

app_name = 'jobscript'

def index(request):
    global myJS
    welcome = "\n\n\n\n\nPhishing is an expansive and costly facet of cyber crime. JobScript utilizes\n an algorithm derived from machine learning techniques to analyze and classify\n fraudulent job listings."
    response = "\n\n\nCopy & Paste it Here to Analyze!"
    submit = "Press Enter to Submit"
    title = "Welcome to JobScript"
    image = False
    homeimage = False

    context = {
        'response': response,
        'welcome': welcome,
        'submit' : submit,
        'title' : title,
        'image': image,
        'homeimage': homeimage,
    }

    userText = request.GET

    if userText == {}:
        #print("2")

        return render(request, 'jobscript/index.html', context)
    else:
        textInput = userText['uTxt']

        runJS = myJS.main(textInput)
        if runJS == False:
            title = "Results"
            welcome = "\n\n\n\n\nGo for it!"
            response = "\n\n\nOur algorithm could not classify this listing as fraudulent."
            submit = "Try another?"
            image = True
            homeimage = False



            context = {
                'response': response,
                'welcome': welcome,
                'submit': submit,
                'title': title,
                'image': image,
                'homeimage': homeimage,
            }
            return render(request, 'jobscript/index.html', context)
        else:
            title = "Results"
            response = "\n\n\n\n\nOur algorithm determined that this listing is likely fraudulent."
            welcome = "Looks sus?"
            submit = "Try another?"
            image = True
            homeimage = False
            context = {
                'response': response,
                'welcome': welcome,
                'submit': submit,
                'title': title,
                'image': image,
                'homeimage': homeimage,
            }
            return render(request, 'jobscript/index.html', context)



