from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapi.http_header_auth import HttpHeaderAuthentication
from myapi.core.models import Role, Privilege

class ListRoles(APIView):
    def get(self, request):
        content = Role.objects.all()
        return Response((content.values()))


class ListPrivileges(APIView):
    def get(self, request):
        content = Privilege.objects.all()
        return Response(content.values())

