from odoo import fields, models


class StockOrderTolerance(models.Model):
    _inherit = 'stock.move'

    tolerance = fields.Float('Tolerance(%)', related="picking_id.partner_id.tolerance")

