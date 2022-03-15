from odoo import models, fields, api, time


class MenuDishes(models.Model):
    _name = 'menu.dishes'
    _description = 'Carito Ardiles Menu'
    _order = 'name, cost_price'
    name = fields.Char('Dish Name')
    cost_price = fields.Float('Dish Price', digits='Dish Price')
    notes = fields.Text('Dish Description')
    ingredients=fields.Many2many(comodel_name='dishes.ingredients',relation='relation_ingr_name', string='Ingredients')
