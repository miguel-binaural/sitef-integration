# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sitef_pos_integration(models.Model):
#     _name = 'sitef_pos_integration.sitef_pos_integration'
#     _description = 'sitef_pos_integration.sitef_pos_integration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100