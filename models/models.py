# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odoo_exam_prixz(models.Model):
    _inherit = 'sale.order'

    rfc = fields.Char(compute='get_rfc')

    #@api.onchange('partner_id')
    def get_rfc(self):
        for record in self:
            default_rfc = 'XAXX010101000'
            if record.partner_id and record.partner_id.vat:
                record.rfc = record.partner_id.vat
            else:
                record.rfc = default_rfc
    # _name = 'odoo_exam_prixz.odoo_exam_prixz'
#     _description = 'odoo_exam_prixz.odoo_exam_prixz'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
