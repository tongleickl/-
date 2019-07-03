from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Book1, Book0, Comment
import json

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":
        test = request.POST
        print(test)
        print(request)
        if test:
            print(test)
            return HttpResponse("ok")
        else:
            print("fail")
            return HttpResponse("fail")
    else:
        rank_list = Book2.objects.all()[:10]
        context = {'rank_list': rank_list}
        return render(request,"book/index.html", context)

def demo1(request):
    book_list = Book2.objects.all()[:5]
    context = {'mbook': book_list}
    return render(request, 'book/book.html',context)

def book(request, book_id):
    mbook = Book0.objects.filter(id = book_id)
    # print(mbook)
    res = {'book': mbook[0].toJSON()}
    # return render(request, 'book/book.html', context)
    return JsonResponse(res)

def newIndex(request):
    if request.method == "POST":
        res = {'code': 0}
        labels = request.POST.get('labels')
        label = labels.split(',')
        if label:
            print(label)
            res['msg'] = '上传成功'
            if len(label) > 1:
                mbook = Book0.objects.filter(category=label[0])
                mbook = mbook.filter(label = label[1]).order_by('-score')[0:8]
            else:
                mbook = Book0.objects.filter(category=label[0]).order_by('-score')[0:8]
            i = 0
            data = []
            for a in mbook:
                data.append(a.toJSON())
            # print(data)
            res['data'] = data

        else:
            print("fail")
        return JsonResponse(res)
    else:
        return render(request, 'index/index.html')

def getdata(request):
    tmp = Book0.objects.values("category").distinct()
    data = []
    for i in tmp:
        num = Book0.objects.filter(category=i['category']).count()
        data.append({'value':num, 'name':i['category']})
    res = {'test':data}
    return HttpResponse(json.dumps(res), content_type='application/json')

def comment(request, book_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        print(content)
        addComment = Comment(book_id = book_id, content = content)
        addComment.save()
    else:
        tmp = Comment.objects.filter(book_id = book_id)
        res = {}
        data = []
        for a in tmp:
            data.append(a.toJSON())
        res['comment'] = data
        return JsonResponse(res)

def comment1(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        content = request.POST.get('content')
        print(content)
        addComment = Comment(book_id = book_id, content = content)
        addComment.save()
        res = {'code': 0}
        return JsonResponse(res)


def ajax_list(request):
    a = [1,2,3]
    res = {'test':a}
    print(res)
    print(json.dumps(res))
    # a = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(res), content_type='application/json')
