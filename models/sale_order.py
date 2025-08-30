# -*- coding: utf-8 -*-

from odoo import models, fields, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Ejecutar la confirmación normal primero
        res = super(SaleOrder, self).action_confirm()
        
        # Verificar si debemos eliminar las transferencias creadas
        for order in self:
            if order.warehouse_id and not order.warehouse_id.create_transfer:
                # Buscar todos los pickings relacionados con esta orden
                pickings = self.env['stock.picking'].search([
                    ('origin', '=', order.name),
                    ('state', 'in', ['draft', 'waiting', 'confirmed', 'assigned'])
                ])
                print("pickings -->", pickings)
                # Cancelar y eliminar los pickings
                pickings.action_cancel()
                pickings.unlink()
        
        return res
    
class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    brand = fields.Char(
        string='Marca',
        related='product_id.product_tmpl_id.x_studio_marca',
        store=True,
        readonly=True
    )
