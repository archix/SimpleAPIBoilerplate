import copy

from .base import base_specs

get_profile_specs = copy.deepcopy(base_specs)
get_profile_specs['responses']['200']['description'] = 'Success'
get_profile_specs['parameters'] = [
    {
        'name': 'Authorization',
        'in': 'header',
        'type': 'string',
        'required': True
    }
]
