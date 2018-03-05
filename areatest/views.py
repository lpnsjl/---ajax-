from django.shortcuts import render
from areatest.models import *
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page


# ajax请求的练习，省市区web开发
def area(request):
    return render(request, 'areatest/area.html')

def pro(request):
    proInfo = AreaInfo.objects.filter(parea__isnull=True)
    list = []
    for pro in proInfo:
        list.append([pro.id,pro.atitle])

    return JsonResponse({'data': list})

def city(request, id):
    cityInfo = AreaInfo.objects.filter(parea__id=id)
    list = []
    for city in cityInfo:
        list.append({'id':city.id, 'atitle':city.atitle})
    return JsonResponse({'data': list})

def dis(request, id):
    disInfo = AreaInfo.objects.filter(parea__id=id)
    list = []
    for dis in disInfo:
        list.append({'id': dis.id, 'atitle': dis.atitle})
    return JsonResponse({'data': list})

# 富文本编辑器练习,使用之前需要去setting中INSTALLED_APPS注册
def editor(request):
    return render(request, 'areatest/editor.html')

def editorhandle(request):
    html = request.POST['content']
    context = {'content':html}
    return render(request, 'areatest/editorhandle.html',context)

# 缓存练习
@cache_page(60*10)

def cacheview(request):
    # return HttpResponse('hello1')
    return HttpResponse('hello')

# 全文检索加中文分词
def mysearch(request):
    return render(request, 'areatest/mysearch.html')

