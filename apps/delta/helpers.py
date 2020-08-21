import pytz
from django.forms.models import model_to_dict
from django.utils import timezone


def model_to_dict_verbose(instance, exclude=("id")):
    dic = model_to_dict(instance, exclude=exclude)
    fields = {f.name: f for f in instance._meta.fields}
    verbose_dic = {}
    for k, v in dic.items():
        field = fields[k]
        key = field.verbose_name[:30]
        value = str(v)
        if hasattr(field, "choices") and fields[k].choices:
            value = dict(fields[k].choices).get(v, "")

        if field.get_internal_type() in ["DateField"]:
            if v:
                value = v.strftime("%d/%m/%Y")

        if field.get_internal_type() in ["DateTimeField"]:
            if v:
                v = timezone.localtime(v, pytz.timezone("America/Fortaleza"))
                value = v.strftime("%d/%m/%Y %H:%M")

        if v is None:
            value = "-"

        verbose_dic[key] = value

    return verbose_dic
