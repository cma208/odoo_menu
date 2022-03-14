from odoo import models, fields, api, time


class RestaurantMenuOrders(models.TransientModel):
    _name = 'restaurant.menu.orders.wizard'
    # _inherit='menu.dishes'

    client_name = fields.Char('Client Name')
    table_number = fields.Integer('Table Number')
    menu_dishes = fields.Many2many('menu.dishes', string='Orders')
    order_date = fields.Date(default=fields.Date.today)


    def add_menu_orders(self):
        self.env['pending.orders'].create({
            'order_date': self.order_date,
            'table_number': self.table_number,
            'client_name': self.client_name,
            'menu_dishes': self.menu_dishes,
        })
