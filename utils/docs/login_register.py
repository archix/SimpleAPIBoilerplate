import copy

from .base import base_specs, base_parameters

register_specs = copy.deepcopy(base_specs)
confirm_register_specs = copy.deepcopy(base_specs)
login_specs = copy.deepcopy(base_specs)

register_specs['responses']['201'] = register_specs['responses']['200']
register_specs['responses']['201']['description'] = 'Successfully registered'
register_specs['parameters'] = base_parameters[:]


confirm_register_specs['parameters'] = [
    {
        'name': 'token',
        'in': 'body',
        'type': 'string'
    }
]

login_specs['parameters'] = base_parameters[0:2]
login_specs['responses']['200']['description'] = 'Successfully login'
login_specs['responses']['200']['schema'] = {
    'Response': {
        'type': 'object',
        'properties': {
            'token': {
                'type': 'string'
            }
        }
    }
}
