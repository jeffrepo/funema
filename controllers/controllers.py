# -*- coding: utf-8 -*-
# from odoo import http


# class Funema(http.Controller):
#     @http.route('/funema/funema', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/funema/funema/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('funema.listing', {
#             'root': '/funema/funema',
#             'objects': http.request.env['funema.funema'].search([]),
#         })

#     @http.route('/funema/funema/objects/<model("funema.funema"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('funema.object', {
#             'object': obj
#         })

