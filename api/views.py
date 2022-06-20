import http

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import CheckList, CheckListItem
from .serializers import CheckListSerializers, CheckListItemSerializer
from .permissions import IsOwner


# from django.http import Http404


class TestAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response({
            "name": "John",
            "type": "Class based view to avoid decorators!!"
        })


class CheckListsAPIView(ListCreateAPIView):
    serializer_class = CheckListSerializers
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

    """
    Listing Checklist and Creating
    """

    # def get(self, request):
    #     data = CheckList.objects.filter(user=request.user)
    #     serializer = self.serializer_class(data, many=True)
    #     serialized_data = serializer.data
    #     return Response(serialized_data)
    #
    # def post(self, request):
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data, context={
    #         'request': request
    #     })
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=http.HTTPStatus.CREATED)
    #     return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)


class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListSerializers
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

    """
    Update, Get, Delete a CheckList
    """

    # def get_object(self, pk):
    #     try:
    #         obj = CheckList.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except CheckList.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     serializer = self.serializer_class(self.get_object(pk))
    #     return Response(serializer.data, status=http.HTTPStatus.ACCEPTED)
    #
    # def put(self, request, pk):
    #     checklist = self.get_object(pk)
    #     serializer = self.serializer_class(checklist, data=request.data, context={
    #         'request': request
    #     })
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=http.HTTPStatus.ACCEPTED)
    #     return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     checklist = self.get_object(pk)
    #     checklist.delete()
    #     return Response(status=http.HTTPStatus.NO_CONTENT)


class CheckListItemsAPIView(ListCreateAPIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset

    """
    List, Create  a CheckList Item
    """

    # def get(self, request):
    #     serializer = self.serializer_class(CheckListItem.objects.all(), many=True)
    #     return Response(serializer.data, status=http.HTTPStatus.OK)
    #
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data, context={
    #         'request': request
    #     })
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=http.HTTPStatus.CREATED)
    #     return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)


class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset

    """
    Retrieve, Update and Destroy  a CheckList Item
    """

    # def get_object(self, pk):
    #     try:
    #         return CheckListItem.objects.get(pk=pk)
    #     except CheckListItem.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     serializer = self.serializer_class(self.get_object(pk))
    #     return Response(serializer.data, status=http.HTTPStatus.ACCEPTED)
    #
    # def put(self, request, pk):
    #     checklistitem = self.get_object(pk)
    #     serializer = self.serializer_class(checklistitem, data=request.data, context={
    #         'request': request
    #     })
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=http.HTTPStatus.ACCEPTED)
    #     return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     checklistitem = self.get_object(pk)
    #     checklistitem.delete()
    #     return Response(status=http.HTTPStatus.NO_CONTENT)
