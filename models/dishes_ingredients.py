from odoo import models, fields, api, time


class DishesIngredients(models.Model):
    _name='dishes.ingredients'
    _description='Ingredients'
    #_order='name'
    ingr_name=fields.Char('Ingredient Name')
    portion_desc=fields.Char('Portion Description')