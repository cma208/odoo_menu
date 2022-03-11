from odoo import models, fields, api, time

class RestaurantMenuOrders(models.TransientModel):
    _name='restaurant.menu.orders.wizard'
    #_inherit='menu.dishes'

    client_name=fields.Char('Client Name')
    table_number=fields.Integer('Table Number')
    menu_dishes=fields.Many2many('menu.dishes', string='Orders')
    order_date = fields.Date(default=fields.Date.today)

