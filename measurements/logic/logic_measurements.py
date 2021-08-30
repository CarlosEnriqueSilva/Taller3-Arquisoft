from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(pPk):
    measurement = Measurement.objects.get(pk = pPk)
    return measurement

def delete_measurement(pPk):
    measurement = Measurement.objects.filter(pk = pPk).delete()
    elimino = measurement[0]
    return elimino


def update_measurement(pPk, val, un, pl):
    cambiar = get_measurement(pPk)
    cambiar.value = val
    cambiar.unit = un
    cambiar.place = pl
    cambiar.save()
    return cambiar