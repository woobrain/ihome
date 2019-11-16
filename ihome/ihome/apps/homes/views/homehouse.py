import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from homes.models import House
from utils.response_code import RET

logger = logging.getLogger("django")


class HomeHouseView(APIView):
    """首页房屋推荐/api/v1.0/houses/index"""

    def get(self, request):

        try:
            houses_obj = House.objects.filter().order_by("-order_count")[0:5]
        except Exception as e:
            logger.error(e)
            return Response({
                "data": {},
                "errmsg": "数据库异常",
                "errno": RET.DBERR
            })
        else:
            data = []
            for house in houses_obj:
                data.append({
                    "house_id": house.id,
                    "img_url": house.index_image_url,
                    "title": house.title
                })

            content = {
                "data": data,
                "errmsg": "ok",
                "errno": RET.OK
            }
        return Response(content)
