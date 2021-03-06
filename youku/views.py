from django.shortcuts import render
from django.http.response import HttpResponse
from youku import YouKu

# Create your views here.



def youku_list(request):
    url = request.GET.get("url","")
    if not url:
        return HttpResponse("pls with url parameter")

    content = ""
    yk = YouKu()
    yk.getList(url)
    content = "<h1><a href=%s>%s</a></h1>" % (yk.url, yk.name)
    content += "<h2>%d</h2>" % (yk.videos.__len__())
    for item in yk.videos:
        content = content + "%02d;<a href=%s>%s</a><br/>" % (int(item[0]),item[1], item[1])
    return HttpResponse(content)
