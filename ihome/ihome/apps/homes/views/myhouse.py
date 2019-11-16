import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from homes.models import House
from utils.response_code import RET

logger = logging.getLogger("django")


class MyHouseView(APIView, LoginRequiredMixin):
    """获取登陆用户的房屋列表 /api/v1.0/user/houses"""
    def get(self, request):
        user = request.user
        try:
            houses_obj = House.objects.filter(user=user)
        except Exception as e:
            logger.error(e)
            return Response({
                "data": {},
                "errmsg": "用户数据异常",
                "errno": RET.DBERR
            })
        else:
            houses = []
            for house in houses_obj:
                houses.append({
                    "address": house.address,
                    "area_name": house.area,
                    "ctime": house.create_time,
                    "house_id": house.id,
                    "img_url": house.index_image_url,
                    "order_count": house.order_count,
                    "price": house.price,
                    "room_count": house.room_count,
                    "title": house.title,
                    "user_avatar": user.avatar
                })

            content = {
                "data": {"houses": houses},
                "errmsg": "ok",
                "errno": RET.OK
            }
        return Response(content)
