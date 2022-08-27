from odoo import api, fields, models, _


class Amount(models.Model):
    _inherit = 'sale.order'
    _description = "Amount"

    discount_amount = fields.Integer(string="Discount")
    total_amount_after_discount = fields.Integer(string="Total Amount After Discount", compute='_compute_total123',
                                                 store=True)

    @api.depends('discount_amount')
    def _compute_total123(self):
        for rec in self:
            if rec.discount_amount:
                rec.total_amount_after_discount = rec.amount_total - rec.discount_amount
            else:
                rec.discount_amount = 1
