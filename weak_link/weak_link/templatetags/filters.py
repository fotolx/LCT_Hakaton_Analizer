from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_percent(dictionary, key):
    return f'{round(dictionary.get(key))}%'