# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/authTimeIp(http.Controller):
#     @http.route('/custom/auth_time_ip/custom/auth_time_ip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/auth_time_ip/custom/auth_time_ip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/auth_time_ip.listing', {
#             'root': '/custom/auth_time_ip/custom/auth_time_ip',
#             'objects': http.request.env['custom/auth_time_ip.custom/auth_time_ip'].search([]),
#         })

#     @http.route('/custom/auth_time_ip/custom/auth_time_ip/objects/<model("custom/auth_time_ip.custom/auth_time_ip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/auth_time_ip.object', {
#             'object': obj
#         })
