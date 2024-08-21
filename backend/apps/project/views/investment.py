from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Investment
from project.serializers.investment import InvestmentSerializer


class InvestmentListCreateView(APIView):

    def get(self, request):
        queryset = Investment.objects.filter(is_deleted=False).all()
        serializer = InvestmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvestmentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InvestmentDetailView(APIView):

    def get(self, request, pk):
        investment = Investment.objects.get(pk=pk, is_deleted=False)
        serializer = InvestmentSerializer(investment)
        return Response(serializer.data, status=status.HTTP_200_OK)
