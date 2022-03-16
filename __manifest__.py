{
    'name': 'My Restaurant',
    'summary': "Check Our New Menu",
    'autor': "Carlos Machicado",
    'website': "http://www.example.com",
    'category': 'Accounting',
    'version': '14',
    'depends': ['base', 'sale', 'point_of_sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        # 'data/data.dishes.csv',
        'views/menu_dishes.xml',
        'views/pending_orders.xml',
        'views/dishes_ingredients.xml',
        'wizard/menu_orders.xml',
    ],
    # 'demo': ['demo.xml'],
    'qweb': [
        'static/src/xml/pos_demo.xml'
    ]
}
