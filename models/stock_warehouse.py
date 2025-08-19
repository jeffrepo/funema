# -*- coding: utf-8 -*-

from odoo import models, fields, _

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    create_transfer = fields.Boolean(string="Crear transferencia?", default=False)