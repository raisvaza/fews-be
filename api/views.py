from django.db.models import Max, F
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, Pos, Reading, Predict
from .serializers import ItemSerializer, PosSerializer, ReadingSerializer, PredictSerializer


@api_view(['GET'])
def getItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_pos(request):
    pos = Pos.objects.all()
    serializer = PosSerializer(pos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reading(request):
    reading = Reading.objects.all()
    serializer = ReadingSerializer(reading, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_predict(request):
    predict = Predict.objects.all()
    serializer = PredictSerializer(predict, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_latest_predict_for_every_pos(request):

    pos_all = Pos.objects.filter(tipe = "DugaAir")

    latest_predict = []

    for pos in pos_all:
        predict = Predict.objects.filter(pos_id = pos).order_by('predict_for').first()
        latest_predict.append(predict)

    print(latest_predict)



    # predict = Predict.objects.all()

    # most_recent_predicts = Predict.objects.values('pos_id_id').annotate(
    #     max_predict_at=Max('predict_for')
    # ).filter(
    #     predict_for=F('max_predict_at')
    # )


    serializer = PredictSerializer(latest_predict, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reading_rainfall(request):
    pos_rainfall = Pos.objects.filter(tipe="CurahHujan")

    limit = request.GET.get("limit")

    reading_rainfall_for_all_pos = []
    for pos in pos_rainfall:
        readings = Reading.objects.filter(tipe="CurahHujan", pos_id=pos).order_by('-reading_at')[:int(limit)]
        serializer = ReadingSerializer(readings, many=True)
        reading_data = {
            "pos_id": pos.id,
            "readings": serializer.data
        }
        reading_rainfall_for_all_pos.append(reading_data)

    return Response(reading_rainfall_for_all_pos)

@api_view(['GET'])
def get_reading_waterlevel(request):
    pos_rainfall = Pos.objects.filter(tipe="DugaAir")

    limit = 7
    if request.GET.get("limit") != None:
        limit = request.GET.get("limit")

    reading_rainfall_for_all_pos = []
    for pos in pos_rainfall:
        readings = Reading.objects.filter(tipe="TinggiAir", pos_id=pos).order_by('-reading_at')[:int(limit)]
        serializer = ReadingSerializer(readings, many=True)
        reading_data = {
            "pos_id": pos.id,
            "readings": serializer.data
        }
        reading_rainfall_for_all_pos.append(reading_data)

    return Response(reading_rainfall_for_all_pos)
