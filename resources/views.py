from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


class ListResources(APIView):
    def get(self, request):
        unprocessed_data = Resource.objects.all()
        data = []
        for emp in unprocessed_data:
            inner = {}
            inner["resource_name"] = emp.resource_name
            inner["model"] = emp.model
            inner["qty"] = emp.qty
            inner["per_qty_value"] = emp.per_qty_value
            data.append(inner)

            # data.append({"name":, "":emp.role, "":emp.team.team_name})
        return Response({
            "status": 200,  
            "data": data
        })
