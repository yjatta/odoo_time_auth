# -*- coding: utf-8 -*-
from datetime import datetime
import logging
from odoo import models, fields, api,SUPERUSER_ID
from odoo.exceptions import AccessDenied
from odoo.http import request, SessionExpiredException

_logger = logging.getLogger(__name__)

_states = [('sunday', 'Sunday'), ('monday','Monday'), ('tuesday', 'Tuesday'),
           ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'),
           ('saturday', 'Saturday')]

class AuthCompany(models.Model):
    _inherit = 'res.company'
    time_auth = fields.Boolean("Auth Time")
    from_time = fields.Float("From")
    to_time = fields.Float("To")
    ip_auth = fields.Boolean("IP Auth")
    country = fields.Many2one('res.country', string='Country')
    ip_domain = fields.Char("IP Domain")


class Days(models.Model):
    _name = 'res.days'

    name = fields.Selection(selection=_states, string='name')
    index = fields.Integer()
