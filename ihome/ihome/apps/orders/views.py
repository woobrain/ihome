# from django.views.decorators.csrf import csrf_exempt
import datetime

import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
# from rest_framework.response import Response
# from rest_framework.views import APIView


from homes.models import House
from orders.models import Order

# from orders.serializers.orders import OrderSerializer

# LoginRequiredMixin
from users.models import User


class OrderView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({"errno": "4101","errmsg": "请先登录"})
        role = request.GET.get('role')

        orders_list = []
        if role == 'custom':
            orders = Order.objects.filter(user=user)
            for order in orders:
                house = House.objects.get(id=order.house_id)
                orders_list.append({
                    "amount": order.amount,
                    "comment": order.comment,
                    "ctime": order.create_time,
                    "days": order.days,
                    "end_date": order.end_date,
                    "img_url": 'aa',
                    "order_id": order.id,
                    "start_date": order.begin_date,
                    "status": order.ORDER_STATUS_ENUM[order.status],
                    "title": house.title
                })
        else:
            houses = House.objects.filter(user=user)
            for house in houses:
                orders = Order.objects.filter(house_id=house.id)
                for order in orders:
                    orders_list.append({
                        "amount": order.amount,
                        "comment": order.comment,
                        "ctime": order.create_time,
                        "days": order.days,
                        "end_date": order.end_date,
                        "img_url": 'aa',
                        "order_id": order.id,
                        "start_date": order.begin_date,
                        "status": order.ORDER_STATUS_ENUM[order.status],
                        "title": house.title
                    })

        return JsonResponse({
            'data': {
                'orders': orders_list
            },
            'errmsg': 'OK',
            'errno': '0',
        })

    def put(self, request, id):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({"errno": "4101","errmsg": "请先登录"})
        action = json.loads(request.body.decode())
        if action.get('action'):
            order = Order.objects.get(id=id)
            if action.get('action') == 'accept':

                order.status = 3
                order.save()
            else:
                order.comment = action.get('reason')
                order.status = 6
                order.save()
            return JsonResponse({
                "errno": "0",
                "errmsg": "操作成功"
            })
        elif action.get('comment'):
            order = Order.objects.get(id=id)
            order.status = 4
            order.comment = action.get('comment')
            order.save()
            return JsonResponse({
                "errno": "0",
                "errmsg": "操作成功"
            })

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({"errno": "4101","errmsg": "请先登录"})
        # user = User.objects.get(user=user)
        house_id = request.POST.get('house_id')
        house = House.objects.get(id=house_id)
        if user == house.user:
            return JsonResponse({"errno": "5555","errmsg": "不能预定自己的房源"})
        s_date = request.POST.get('start_date')
        e_date = request.POST.get('end_date')

        start_date = datetime.datetime.strptime(s_date, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(e_date, '%Y-%m-%d').date()

        start_sec = (start_date - datetime.date(1970, 1, 1)).total_seconds()
        end_sec = (end_date - datetime.date(1970, 1, 1)).total_seconds()
        if start_sec >= end_sec:
            return JsonResponse({"errno": "5555","errmsg": "结束日期应该大于起始日期"})
        days = int((end_sec - start_sec) / 3600 / 24)
        house = House.objects.get(id=house_id)
        amount = house.price * days
        # user = User.objects.get(id=8)
        order = Order.objects.create(user=user,
                                     house_id=house_id,
                                     begin_date=start_date,
                                     end_date=end_date,
                                     house_price=house.price,
                                     amount=amount,
                                     days=days,
                                     status=0)
        return JsonResponse({
            "data": {
                "order_id": order.id
            },
            "errno": "0",
            "errmsg": "下单成功"
        })
