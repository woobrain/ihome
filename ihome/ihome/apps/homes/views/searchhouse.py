import logging

from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from homes.models import House, Area
from utils import constants
from utils.response_code import RET

logger = logging.getLogger("django")


class SearchHouseView(APIView):
    """房屋数据搜索 /api/v1.0/houses"""

    def get(self, request):

        data = request.query_params
        aid = data.get('aid', '')
        sd = data.get('sd', '')
        ed = data.get('ed', '')
        sk = data.get('sk', '')
        p = data.get('sk', 1)

        if not (aid or sd or ed or sk):
            try:
                houses_obj = House.objects.all().order_by('-create_time')
            except Exception as e:
                logger.error(e)
                return Response({
                    "data": {},
                    "errmsg": "数据异常",
                    "errno": RET.DBERR
                })
            else:
                paginator = Paginator(houses_obj, constants.HOUSE_LIST_PAGE_CAPACITY)
                # 获取当前页对象
                page_houses = paginator.page(p)
                # 获取总页数
                total_page = paginator.num_pages
                houses = []
                for house in page_houses:
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
                        "user_avatar": Area.object.get(user=house.user)
                    })

                data = {
                    "total_page": total_page,
                    "houses": houses
                }

                content = {
                    "data": data,
                    "errmsg": "ok",
                    "errno": RET.OK
                }
                return Response(content)
        # 校验参数
        if sd and ed:
            pass