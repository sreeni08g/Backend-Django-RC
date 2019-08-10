from . import models
from rest_framework import serializers


class QueryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QueryHistory
        fields = '__all__'
        read_only_fields = ('date_created','date_modified')
