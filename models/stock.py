from odoo import models, _


class StockTolerance(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for rec in self.move_ids_without_package:
            tolerance_rate = int(rec.product_uom_qty * (rec.tolerance / 100))
            maximum_rate = rec.product_uom_qty + tolerance_rate
            minimum_rate = rec.product_uom_qty - tolerance_rate
        if (rec.quantity_done > maximum_rate) or (rec.quantity_done < minimum_rate):
            return {
                'name': _('Validation Wizard'),
                'type': 'ir.actions.act_window',
                'res_model': 'model.wizard',
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'new'
            }
        else:
            res = super(StockTolerance, self).button_validate()
            return res

