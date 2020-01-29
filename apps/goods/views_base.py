

from django.views.generic.base import View

from goods.models import *


class GoodsListView(View):

    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        import json
        goods = Goods.objects.all()[:10]
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import JsonResponse
        return JsonResponse(json_data, safe=False)