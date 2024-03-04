# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stockPicking(models.Model):
    _inherit = 'stock.picking'

    reservado_total = fields.Float(compute='get_reservado')

    #@api.onchange('partner_id')
    def get_reservado(self):
        print("reservado")
        for record in self:
            reservado = 0.0
            if len(record.move_line_ids):
                for line in record.move_line_ids:
                    reservado += line.product_id.qty_available - line.product_id.free_qty
            if reservado > 0:
                record.reservado_total = reservado
                print("reservado: ",record.reservado_total)
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
