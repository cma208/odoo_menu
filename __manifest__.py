{
    'name': 'My Restaurant',
    'summary': "Check Our New Menu",
    'autor': "Carlos Machicado",
    'website': "http://www.example.com",
    'category': 'Restaurant',
    'version': '14',
    'depends': ['base', 'sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/data.dishes.csv',
        'views/menu_dishes.xml',
    ],
    'demo': ['demo.xml'],
}