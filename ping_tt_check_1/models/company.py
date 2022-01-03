# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    # here, key has to be full xmlID(including the module name) of all the
    # new report actions that you have defined for check layout
    ping_account_check_printing_layout = fields.Selection(selection_add=[
        ('ping_tt_check_1.action_print_check_top', 'Print Check (Top) - PING TT'),
        ('ping_tt_check_1.action_print_check_middle', 'Print Check (Middle) - PING TT'),
        ('ping_tt_check_1.action_print_check_bottom', 'Print Check (Bottom) - PING TT'),
    ], ondelete={
        'ping_tt_check_1.action_print_check_top': 'set default',
        'ping_tt_check_1.action_print_check_middle': 'set default',
        'ping_tt_check_1.action_print_check_bottom': 'set default',
    })
