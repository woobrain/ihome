
from rest_framework.response import Response
from rest_framework.views import APIView

from homes.models import Area, House


class HousesView(APIView):
    def post(self,request):
        data=request.data
        user=data.user
        house_id=user.id
        house=House.objects.create(
            house_id=house_id,
            user=user,
            area=data.area,
            title=data.title,
            price=data.price,
            address=data.address,
            room_count=data.room_count,
            acreage=data.acreage,
            unit=data.unit,
            capacity=data.capacity,
            beds=data.beds,
            deposit=data.deposit,
            min_days=data.min_days,
            max_days=data.max_days,
            order_count=data.order_count,
            index_image_url=data.index_image_url,
            facility=data.facility
        )
        house.save()
        return Response({'errmsg':'发布成功','errno':'errno','data':house_id})
