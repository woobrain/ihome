from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from homes.models import Area
class AreasListView(APIView):
    def get(self,request):
        areas=Area.objects.all()
        data=[]
        for area in areas:
            data.append({
                'aid':area.id,
                'aname':area.name
            })

        return Response({'errmsg':'获取成功','errno':'0','data':data})

