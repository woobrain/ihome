import logging

from django.http import JsonResponse
from django.views import View
from homes.models import House
from utils.response_code import RET

logger = logging.getLogger("django")


class HouseDetailView(View):
    """房屋详情 /api/v1.0/houses/[int:house_id]"""

    def get(self, request, houseid):
        try:
            house = House.objects.filter(id=houseid)
        except Exception as e:
            logger.error(e)
            return JsonResponse({
                "house": {},
                "errmsg": "数据异常",
                "errno": RET.PARAMERR
            })

        else:
            user = request.user
            data = {"house": {"house": {
                "acreage": 5,
                "address": "我是地址",
                "beds": "5张床",
                "capacity": 5,
                "comments": [
                    {
                        "comment": "哎哟不错哟",
                        "ctime": "2017-11-14 11:17:07",
                        "user_name": "匿名用户"
                    }
                ],
                "deposit": 500,
                "facilities": [
                    1
                ],
                "hid": 4,
                "img_urls": [
                    "http://oyucyko3w.bkt.clouddn.com/FhgvJiGF9Wfjse8ZhAXb_pYObECQ",
                    "http://oyucyko3w.bkt.clouddn.com/FkagyA8TiuxnLsz7ofLfA_CY34Nw"
                ],
                "max_days": 5,
                "min_days": 5,
                "price": 500,
                "room_count": 5,
                "title": "555",
                "unit": "5",
                "user_avatar": "http://oyucyko3w.bkt.clouddn.com/FmWZRObXNX6TdC8D688AjmDAoVrS",
                "user_id": user.id,
                "user_name": "哈哈哈哈哈哈"
            },
                "user_id": user.id}}
            content = {
                "data": data,
                "errmsg": "数据异常",
                "errno": RET.OK
            }
