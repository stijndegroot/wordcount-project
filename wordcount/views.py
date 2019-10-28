from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def countpage(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordcount = {}
    # Counting the words
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'countpage.html', {'fulltext': fulltext, 'count': len(wordlist),
                                              'sortedwords': sortedwords})
