import copy

from .base import base_specs, base_parameters

add_user_specs = copy.deepcopy(base_specs)

add_user_specs['responses']['201'] = add_user_specs['responses']['200']
add_user_specs['responses']['201']['description'] = 'Successfully added'
add_user_specs['parameters'] = base_parameters[:]
add_user_specs['parameters'].append({
    'name': 'Authorization',
    'in': 'header',
    'type': 'string',
    'required': True
})
