{
    'name': 'Runbot PS extension',
    'category': 'Website',
    'summary': 'Runbot PS extension',
    'version': '2.0',
    'description': "Runbot PS extension",
    'author': 'Odoo SA',
    'depends': ['runbot'],
    'data': [
        'data/runbot_build_config_data.xml',
        'data/cron.xml',
        'views/repo.xml',
        'views/runbot_build_config.xml',
        'views/templates.xml',
    ],
}