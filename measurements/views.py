from .logic.logic_measurements import get_all_measurements, get_measurement, delete_measurement, update_measurement
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list,content_type='application/json')


def get_one_measurement(request, pPk):
    measurement = get_measurement(pPk)
    measurement_json = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_json, content_type = 'application/json')

def delete_one_measurement(request, pPk):
    cantidad = delete_measurement(pPk)
    return HttpResponse("Se eliminaron " + str(cantidad) + " valor de medidas")


def update_one_measurement(request, pPk, val, un, pl):
    cambiar = update_measurement(pPk, val, un, pl)
    cambiar_json = serializers.serialize('json',[cambiar])
    return HttpResponse(cambiar_json, content_type = 'application/json')