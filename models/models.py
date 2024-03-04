# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo_exam_prixz(models.Model):
    _inherit = 'sale.order'

    rfc = fields.Char(compute='get_rfc')

    def get_rfc(self):
        for record in self:
            default_rfc = 'XAXX010101000'
            if record.partner_id and record.partner_id.vat:
                record.rfc = record.partner_id.vat
            else:
                record.rfc = default_rfc