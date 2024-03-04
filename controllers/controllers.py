# -*- coding: utf-8 -*-
# from odoo import http


# class OdooExamPrixz(http.Controller):
#     @http.route('/odoo_exam_prixz/odoo_exam_prixz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_exam_prixz/odoo_exam_prixz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_exam_prixz.listing', {
#             'root': '/odoo_exam_prixz/odoo_exam_prixz',
#             'objects': http.request.env['odoo_exam_prixz.odoo_exam_prixz'].search([]),
#         })

#     @http.route('/odoo_exam_prixz/odoo_exam_prixz/objects/<model("odoo_exam_prixz.odoo_exam_prixz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_exam_prixz.object', {
#             'object': obj
#         })
