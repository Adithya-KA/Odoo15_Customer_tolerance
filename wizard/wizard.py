from odoo import fields, models


class Wizard(models.TransientModel):
    _name = 'model.wizard'
    _description = 'wizard'

    warning = fields.Text(default='The quantity to be validated is either less than minimum tolerance range or greater than the maximum tolerance range', readonly=1)

    def action_accept(self):
        action_picking = self.env['stock.picking'].browse(self.env.context.get('active_ids'))
        action_picking._action_done()
