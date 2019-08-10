from rest_framework import generics
from .serializers import QueryHistorySerializer
from .models import QueryHistory


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = QueryHistory.objects.all()
    serializer_class = QueryHistorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class GetView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = QueryHistory.objects.all()
    serializer_class = QueryHistorySerializer