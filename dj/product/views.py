from django.views import View
from django.http import JsonResponse, FileResponse
from .models import Product
import json
from django.core import serializers
from .saveTable import export_to_excel
from django.db.models import Q
from .models import Product


def CreateProductView(request):
    data = json.loads(request.body)  # 解码并加载JSON数据
    print(data)
    return JsonResponse({'msg': '添加成功', 'code': 200}, json_dumps_params={'ensure_ascii': False})


def searchProduct(request):
    # print(request.body)
    data = json.loads(request.body)  # 解码并加载JSON数据
    # print(data)
    if data['option']:
        options = data['option']
        print(options)
        products = Product.objects.all()
        conditions = []
        for key, value in options.items():
            if value:
                conditions.append(Q(**{key: value}))

        if conditions:
            products = products.filter(*conditions)
        result = []
        for item in products:
            result.append({
                'id': item.id,
                "name": item.name,
                "specification": item.specification,
                "level": item.level,
                "weight": item.weight,
                "kind": item.kind
            })
        return JsonResponse({'msg': result, 'code': 200}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'msg': '查询失败', 'code': 400}, json_dumps_params={'ensure_ascii': False})


def saveTable(request):
    try:
        data = json.loads(request.body)
        table = data['table']

        print(table)

        # return JsonResponse({'msg': table, 'code': 200}, json_dumps_params={'ensure_ascii': False})
        update_file_path = export_to_excel(table)
        file = open(update_file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        # file_name下载下来保存的文件名字
        content_dis = 'attachment;filename=' + update_file_path.split('/')[-1]
        response["Access-Control-Expose-Headers"] = "Content-Disposition"

        response['Content-Disposition'] = content_dis
        return response
    except:
        return JsonResponse({'msg': '保存失败', 'code': 400}, json_dumps_params={'ensure_ascii': False})
