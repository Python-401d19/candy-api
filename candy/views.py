from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Candy
from .permissions import IsOwnerOrReadOnly
from .serializers import CandySerializer


class CandyList(ListCreateAPIView):
    queryset = Candy.objects.all()
    serializer_class = CandySerializer


class CandyDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Candy.objects.all()
    serializer_class = CandySerializer
