
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from Piter_Hipster.models import *
from Piter_Hipster.serializers import *

class CatalogAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    #PhotoSerializer - как подключить??
    permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        goods = Goods.objects.all()
        photos=Photos.objects.all()
        goodsSerializer = GoodsBuyerSerializers(goods, many=True)
        photoSerializer = PhotoSerializer(photos, many=True)
        return Response({"goods": goodsSerializer.data,})
                        #"photos": photoSerializer.data})



    # def post(self, request):
    #     task = TaskPostSerializers(data=request.data)
    #     if task.is_valid():
    #         task.save(creator=request.user)
    #         return Response({"status": "Added"})
    #     else:
    #         return Response({"status": "Error"})
