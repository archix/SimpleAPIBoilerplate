import copy

from .base import base_specs, base_parameters

update_specs = copy.deepcopy(base_specs)

update_specs['responses']['200']['description'] = 'Successfully updated'
update_specs['parameters'] = base_parameters[:]
update_specs['parameters'].append({
    'name': 'Authorization',
    'in': 'header',
    'type': 'string',
    'required': True
})

update_another_specs = copy.deepcopy(update_specs)
update_another_specs['parameters'].append({
    'name': 'user_id',
    'in': 'path',
    'type': 'integer',
    'required': True
})
