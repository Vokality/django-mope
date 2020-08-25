from django.conf import settings

_DEFAULTS = {
    'CURRENCIES': ['SRD', 'USD', 'EUR'],
}


def get_setting(setting):
    return getattr(
        settings,
        setting,
        _DEFAULTS[setting]
    )
