# -*- coding: utf-8 -*-

from odoo import models, fields, _

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    brand = fields.Char(
        string='Marca',
        related='product_id.product_tmpl_id.x_studio_marca',
        store=True,  # Depende de tus necesidades
        readonly=True
    )