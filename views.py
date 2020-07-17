from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import serializers
import traceback
from models import (
    Category,
    Subcategory,
    Items,
    Rating,
)

# Declared serializer for category list view class
class CategoryListViewSerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id",
                  "name",
                  "description",
                  "flag",
                  "subcategory",
                  "items",
                  )

    @staticmethod
    def get_subcategory(obj):
        return Subcategory.objects.filter(category_id=obj.id).values()

    @staticmethod
    def get_items(obj):
        return Items.objects.filter(subcategory__category_id=obj.id, rating_gte=4).values()


class CategoryListView(APIView):
    @staticmethod
    def get(request):
        try:
            search = request.GET.get("search", "")
            category_query = Category.objects.filter()
            if search:
                category_query = Category.objects.filter(
                    Q(id__icontains=search) | Q(name__icontains=search))
            serializer = CategoryListViewSerializer(
                instance=category_query, many=True).data
            return Response({"result": serializer}, status.HTTP_200_OK)
        except:
            res = {"message": traceback.format_exc(), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}
            return Response(res, res["status"])

class ItemListView(APIView):
    @staticmethod
    def get(request):
        try:
            search = request.GET.get("search", "")
            item_query = Rating.objects.filter(rating_gte=3).values("item_id","item__name","item__description","rating")
            if search:
                item_query = Rating.objects.filter(
                    Q(id__icontains=search) | Q(name__icontains=search),rating_gte=3 ).values("item_id","item__name","item__description", "rating")
            return Response({"result": item_query}, status.HTTP_200_OK)
        except:
            res = {"message": traceback.format_exc(), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}
            return Response(res, res["status"])
