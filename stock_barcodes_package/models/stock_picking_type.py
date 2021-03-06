# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    def action_barcode_scan(self):
        res = super(StockPickingType, self).action_barcode_scan()
        res['context']['default_picking_type_id'] = self.id
        return res