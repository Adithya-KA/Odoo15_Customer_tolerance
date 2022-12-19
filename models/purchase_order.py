from odoo import fields, models


class PurchaseOrderTolerance(models.Model):
    _inherit = 'purchase.order.line'

    tolerance = fields.Float('Tolerance(%)', related='order_id.partner_id.tolerance')
