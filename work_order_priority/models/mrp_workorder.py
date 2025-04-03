from odoo import models, fields, api

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    priority = fields.Selection(
        related='production_id.priority',
        string='Priority',
        readonly=True,
        store=True
    )
