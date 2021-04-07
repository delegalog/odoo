# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Action(models.Model):
    _name = 'dlg_crm.action'
    _description = 'Acción'

    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha creación')
    date_event = fields.Datetime(string='Fecha evento')
    date_end = fields.Datetime(string='Fecha fin')
    type = fields.Selection([('C', 'Call'), ('R', 'Reunión'), ('L', 'Llamada'),
                             ('D', 'Comida'), ('E', 'email')], string='Tipo', required=False)
    #done = fields.Boolean(string='Finalizada')
    image = fields.Binary(string='Imagen')
    opportunity = fields.Many2one('dlg_crm.opportunity', string="Oportunidad", required=False)
    color = fields.Integer()
    _order = 'date_event asc'

    #def toggle_state(self):
     #   self.done = not self.done

    # ORM
    def f_create(self):
        action = {
            'date': datetime.date.today(),
            'type': 'C',
            'done': False,
            'color': 0,
        }
        print(action)
        self.env['dlg_crm.action'].create(action)

    def f_search_update(self):
        action = self.env['dlg_crm.action'].search([('name', '=', 'ORM test')])
        print('search()', action, action.name)

        action_b = self.env['dlg_crm.action'].browse([8])
        print('browse()', action_b, action_b.name)

        action.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        action = self.env['dlg_crm.action'].browse([8])
        action.unlink()


class ActionReport(models.AbstractModel):
    _name = 'report.dlg_crm.report_action_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_action_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.action'],
            'docs': self.env['dlg_crm.action'].browse(docids)
        }
