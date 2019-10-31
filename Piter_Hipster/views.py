
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.shortcuts import get_object_or_404



from Piter_Hipster.models import *
from Piter_Hipster.serializers import *

class CatalogAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        category = request.GET.get("id_category")
        goods = Goods.objects.filter(id_category = category)
        goodsSerializer = GoodsCatalogSerializers(instance=goods, many=True)
        return Response({"goods": goodsSerializer.data,})

class MainAPI(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        categories = Categories.objects.all()
        categoriesSerializer = CategorySerializer(categories, many = True)
        return Response({"categories": categoriesSerializer.data, })

class GoodsAPI(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        id_goods = request.GET.get("id")
        goods = Goods.objects.filter(id=id_goods)
        goodsSerializer = GoodsBuyerSerializers(goods, many=True)
        return Response({"categories": goodsSerializer.data, })
    # def get(self, request):
    #     orders = Orders.objects.all()
    #     ordersSerializer = OrdersPostSerializer(orders, many=True)
    #     return Response({"orders": ordersSerializer.data, })

    def post(self, request):
        order = OrdersPostSerializer(data=request.data)
        if order.is_valid():
            order.save()
            return Response(status=201)
        else: return Response(status=400)

    # def create(self, request):
    #     # Look up objects by arbitrary attributes.
    #     # You can check here if your students are participating
    #     # the classes and have taken the subjects they sign up for.
    #     goodsInOrders = get_object_or_404(
    #         GoodsInOrders,
    #         Count=request.data.get('Count'),
    #         Price=request.data.get('Price')
    #     )
    #     id_delivery = get_object_or_404(
    #         Delivery,
    #         Type_delivery=request.data.get("Type_delivery"),
    #         Address=request.data.get("Address_delivery"),
    #         Price=request.data.get("Price_delivery")
    #     )
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(goodsInOrders=goodsInOrders, id_delivery=id_delivery)
    #     headers = self.get_success_headers(serializer.data)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
