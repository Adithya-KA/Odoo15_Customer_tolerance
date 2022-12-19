from odoo import fields, models


class ContactTolerance(models.Model):
    _inherit = 'res.partner'

    tolerance = fields.Float('Tolerance(%)')



