from rest_framework import serializers
from base.models import Item, Pos, Reading, Predict

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos
        fields = '__all__'

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'

class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = '__all__'