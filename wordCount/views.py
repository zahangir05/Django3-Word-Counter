from django.shortcuts import render


def home(request):
    # return HttpResponse("Welcome to Django Word Count Home Page!!..")
    return render(request, 'homepage.html')


def count(request):
    text = request.GET['text']
    textList = text.split()
    length = len(textList)
    textDict = {}

    print("LL: {}".format(type(textDict)))
    print("dd: {}".format(type(textDict)))

    for t in textList:
        # print(t, end=", ")
        if t in textDict:
            textDict[t] += 1
        else:
            textDict[t] = 1

    # textDict = {k: v for k, v in sorted(textDict.items(), key=lambda x: x[1], reverse=True)}
    textDict = sorted(textDict.items(), key=lambda x: x[1], reverse=True)
    print(type(textDict))
    return render(request, 'wordCount.html', {'text': text, 'length': length, 'textDict': textDict})


def about(request):
    return render(request, 'about.html')
