from rest_framework import serializers
from .models import Activity, Feature

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Activity
    	fields = ('id', 'name', 'photo_url', 'features',)



class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'photo_url', 'description',)
