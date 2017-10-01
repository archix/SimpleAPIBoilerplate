import copy

from .base import base_specs

get_users_specs = copy.deepcopy(base_specs)
get_users_specs['parameters'] = [
    {
        'name': 'Authorization',
        'in': 'header',
        'type': 'string',
        'required': True
    }
]
get_users_specs['responses']['200']['description'] = 'Success'
get_users_specs['responses']['200']['examples'] = [
    {
        'active': True,
        'details': {
            'address': 'Main Street 11b',
            'avatar': 'path.to.avatar.jpg',
            'date_of_birth': '1991-01-01',
            'gender': 'male',
            'id': 6,
            'phone_number': '+381601234567',
            'postal_code': '11070'
        },
        'email': 'novi.manager2@maildrop.cc',
        'first_name': 'Manager',
        'id': 37,
        'last_name': 'Managerski',
        'role': {
            'id': 2,
            'name': 'Manager'
        }
    },
    {
        'active': True,
        'details': {
            'address': 'Main Street 10',
            'avatar': 'path.to.avatar.jpg',
            'date_of_birth': '1991-01-05',
            'gender': 'male',
            'id': 5,
            'phone_number': '+38160123654',
            'postal_code': '11070'
        },
        'email': 'novi.user@maildrop.cc',
        'first_name': 'John',
        'id': 36,
        'last_name': 'Doe',
        'role': {
            'id': 3,
            'name': 'User'
        }
    }
]
