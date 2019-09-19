# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ks_hide_debug_assets_permission = fields.Boolean(string='Hide Debug Assets',
                                                     config_parameter='ks_hide_debug_assets_permission')

    def set_ks_hide_debug_assets_permission(self):
        self.env['ir.config_parameter'].set_param(
            'ks_hide_debug_assets_permission', self.ks_hide_debug_assets_permission, groups=['base.group_system'])

    def get_default_ks_hide_debug_assets_permission(self, fields):
        ks_hide_debug_assets_permission = self.env['ir.config_parameter'].get_param('ks_hide_debug_assets_permission',
                                                                                    default='')
        return dict(ks_hide_debug_assets_permission=ks_hide_debug_assets_permission)
