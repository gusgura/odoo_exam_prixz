# -*- coding: utf-8 -*-

import requests
import json
from odoo import models, fields, api

class stockPicking(models.Model):
    _inherit = 'stock.picking'

    reservado_total = fields.Float(compute='get_reservado')

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

    def get_products_api(self):
        url = "https://fakestoreapi.com/products"
        # api_key = "a57b8608-76ec-4ec6-8459-fd2e8d962db2"
        # if not self.env['ir.config_parameter'].sudo().get_param('database.is_neutralized', False):
        #     url = self.env['ir.config_parameter'].sudo().get_param('VTECH_Asismed_Medikit.medikit_url', False)
        #     api_key = self.env['ir.config_parameter'].sudo().get_param('VTECH_Asismed_Medikit.medikit_api_key', False)
        # payload = "{\r\n    \"NUR\":\"%s\"\r\n}\r\n"%(nur)
        # headers = {
        #     'API-KEY': api_key
        # }
        response = requests.get(url)#, headers=headers, data=payload)
        content_decode = response.content.decode("utf-8")
        content_json = json.loads(content_decode)
        print("API: ",content_json)
        # if content_json['Error'] != 'OK':
        #     raise UserError(content_json['Error'])
        # return content_json