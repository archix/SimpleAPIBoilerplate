base_specs = {
    'definitions': {
        'User': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'int'
                },
                'email': {
                    'type': 'string'
                },
                'first_name': {
                    'type': 'string'
                },
                'last_name': {
                    'type': 'string'
                },
                'active': {
                    'type': 'boolean'
                },
                'role': {
                    '$ref': '#/definitions/Role'
                },
                'details': {
                    '$ref': '#/definitions/UserDetails'
                }
            }
        },
        'UserDetails': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'int'
                },
                'address': {
                    'type': 'string'
                },
                'phone_number': {
                    'type': 'string'
                },
                'postal_code': {
                    'type': 'string'
                },
                'date_of_birth': {
                    'type': 'string'
                },
                'gender': {
                    'type': 'string'
                },
                'avatar': {
                    'type': 'string'
                }
            }
        },
        'Role': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'int'
                },
                'name': {
                    'type': 'str'
                }
            }
        }
    },
    'responses': {
        '200': {
            'description': '',
            'schema': {
                '$ref': '#/definitions/User'
            },
            'examples': {
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
            }
        }
    }
}

base_parameters = [
    {
        'name': 'email',
        'in': 'body',
        'type': 'string',
    },
    {
        'name': 'password',
        'in': 'body',
        'type': 'string',
    },
    {
        'name': 'first_name',
        'in': 'body',
        'type': 'string',
    },
    {
        'name': 'last_name',
        'in': 'body',
        'type': 'string',
    },
    {
        'name': 'details',
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/UserDetails'
        }
    }
]

