from odoo import models, fields, api


class MenuDishes(models.Model):
    _name = 'menu.dishes'
    _description = 'Carito Ardiles Menu'
    _order = 'name, cost_price'
    name = fields.Char('Dish Name')
    cost_price = fields.Float('Dish Price', digits='Dish Price')
    notes = fields.Text('Dish Description')
