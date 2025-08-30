# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    brand = fields.Char(
        string="Marca",
        readonly=True,
    )

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['brand'] = "l.brand"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += ", l.brand"
        return res
