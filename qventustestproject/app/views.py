from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Part
from .serializer import PartSerializer
from collections import Counter
import re
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    @action(detail=False, methods=['get'])
    def common_words(self, request):
        descriptions = Part.objects.values_list('description', flat=True)
        words = re.findall(r'\w+', ' '.join(descriptions).lower())
        common_words = Counter(words).most_common(5)
        return Response(common_words)