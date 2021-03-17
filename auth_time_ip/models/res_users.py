# -*- coding: utf-8 -*-
from datetime import datetime
import logging
from odoo import models, fields, api,SUPERUSER_ID
from odoo.exceptions import AccessDenied
from odoo.http import request, SessionExpiredException

_logger = logging.getLogger(__name__)

def _time_to_float(time):
    hour = str(time.hour)
    min = str(time.minute)
    hour_min = str(hour + "." + min)
    return float(hour_min)


class AuthTimeIP(models.Model):

    def _get_default_from_company(self):
        pass
    _inherit = 'res.users'
    time_auth = fields.Boolean("Auth Time", help="Enable Time Authentication")
    from_time = fields.Float("From", help="This user cannot login after this time")
    to_time = fields.Float("To", help="This user cannot login before this time")
    ip_auth = fields.Boolean("IP Auth")
    country = fields.Many2one('res.country', string='Country')
    ip_domain = fields.Char("IP Domain")
    days = fields.Many2many('res.days', string="Days")
    index_days = fields.Char(string="Indexes", compute='_get_index_days', store=True)

    @api.depends('days')
    def _get_index_days(self):
        for rec in self:
            rec.index_days = ""
            indexes = ""
            for day in rec.days:
                indexes += str(day.index) + ","
            rec.index_days = indexes.rstrip(",")
    def _check_ip_authentication(self, user, ip):
        ip_list = str(user.ip_domain).split(',')
        if user.ip_auth:
            for ip_address in ip_list:
               if ip_address == ip:
                   return
            raise AccessDenied("Your IP is NOT Authorized")


    def _auth_session_terminate(self,user,session):

        """
        if user has time Auth
             if out of time range
                 perform a clean logout

        :param user: current user
        :param session:
        :return:
        """

        if user.time_auth:
            if self._check_out_of_time(user):
                if session.db and session.uid:
                    session.logout(keep_db=True)
                    raise SessionExpiredException("You Cannot access the system after work hours")
                return True

    def _check_out_of_time(self, user):
        days = user.index_days.split(",")
        for day in days:
            if datetime.now().day == int(day) :
                return True
        time_now = _time_to_float(datetime.now().time())
        now_type = "pm" if time_now >= 12 else "am"
        user_time_from = user.from_time
        from_type = "pm" if user_time_from >= 12 else "am"
        user_time_to = user.to_time
        #
        if user_time_from == user_time_to:
            return False
        to_type = "pm" if user_time_to >= 12 else "am"
        if user_time_from < time_now or from_type != now_type:
            if user_time_to > time_now or to_type != now_type:
                return True
        return False

    def _check_time_authentication(self, user):
        if  user.time_auth:
            if self._check_out_of_time(user):
                raise  AccessDenied("You cannot access the system at this time")

    @classmethod
    def _login(cls, db, login, password):
        if not password:
            raise AccessDenied()
        ip = request.httprequest.environ['REMOTE_ADDR'] if request else 'n/a'
        _logger.info("MY IP: %s", ip)
        try:
            with cls.pool.cursor() as cr:
                self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
                with self._assert_can_auth():
                    user = self.search(self._get_login_domain(login))
                    if not user:
                        raise AccessDenied()
                    user = user.sudo(user.id)
                    user._check_credentials(password)
                    self._check_time_authentication(user)
                    self._check_ip_authentication(user, ip)
                    user._update_last_login()
        except AccessDenied:
            _logger.info("Login failed for db:%s login:%s from %s", db, login, ip)
            raise
        _logger.info("Login successful for db:%s login:%s from %s", db, login, ip)
        return user.id

