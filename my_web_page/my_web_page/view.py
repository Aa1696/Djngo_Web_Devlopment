from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'home.html')


def new_func(response):
    data_read = response.GET['count_the_word']
    data_list = data_read.split()
    dict1 = {}
    for i in data_list:
        if (i in dict1):
            dict1[i] += 1
        else:
            dict1[i] = 1

    return render(response, 'count.html',
                  {'count_the_words': len(data_list), 'text': data_read, 'freq_of_words': dict1})


def about_us(response):
    return render(response, 'aboutus.html')
