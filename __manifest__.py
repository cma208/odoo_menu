{
    'name': 'My Restaurant',
    'summary': "Check Our New Menu",
    'autor': "Carlos Machicado",
    'website': "http://www.example.com",
    'category': 'Accounting',
    'version': '14',
    'depends': ['base', 'sale'],
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'wizard/menu_orders.xml',
        # 'data/data.dishes.csv',
        'views/menu_dishes.xml',
        'views/pending_orders.xml',
        'views/dishes_ingredients.xml'
    ],
    # 'demo': ['demo.xml'],
}
