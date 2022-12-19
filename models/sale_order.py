from odoo import fields, models


class SaleOrderLineTolerance(models.Model):
    _inherit = 'sale.order.line'

    tolerance = fields.Float('Tolerance(%)', related='order_id.partner_id.tolerance')

