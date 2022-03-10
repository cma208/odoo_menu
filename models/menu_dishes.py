from odoo import models, fields, api


class MenuDishes(model.Model):
    _name='menu.dishes'
    _description='Carito Ardiles Menu'
    _order='name, cost_price'
    cost_price=fields.Float('Dish Price', digits='Dish Price')
    notes=fields.Text('Dish Description')