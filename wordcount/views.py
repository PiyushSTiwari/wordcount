from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    data= request.GET['fulltextarea']
    data_list=data.split()
    total_word=len(data_list)
    word_dict={}
    for i in data_list:
        if i in word_dict:
            word_dict[i]+=1
        else:
            word_dict[i]=1
    word_dict=sorted(word_dict.items())

    return render(request, 'count.html',{'data_list':data_list,'total_word':total_word, 'word_dict':word_dict})

def about(request):
    return render(request, 'about.html')