# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class TestView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        return Response({'foo': 'bar'})


test_view = TestView.as_view()
