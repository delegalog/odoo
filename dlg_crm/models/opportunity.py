# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Opportunity(models.Model):
    _name = 'dlg_crm.opportunity'
    _description = 'Opportunity'

    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('C', 'Call'), ('P', 'Presencial'), ('T', 'Telefónico'),
                             ('G', '-')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')
    phase = fields.Many2one('dlg_crm.phase', string="Fase", required=True)
    color = fields.Integer()

    header = fields.boolean(requiered=True)
    volume_year = fields.Long()
    orders_year = fields.Long()

    def toggle_state(self):
        self.done = not self.done

    #ORM
    def f_create(self):
        opportunity = {
            'name': 'ORM test',
            'notes': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'C',
            'status': '0',
            'done': False,
            'color': 0
        }
        print(opportunity)
        self.env['dlg_crm.opportunity'].create(opportunity)

    def f_search_update(self):
        opportunity = self.env['dlg_crm.opportunity'].search([('name', '=', 'ORM test')])
        print('search()', opportunity, opportunity.name)

        opportunity_b = self.env['dlg_crm.opportunity'].browse([8])
        print('browse()', opportunity_b, opportunity_b.name)

        opportunity.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        opportunity = self.env['dlg_crm.opportunity'].browse([8])
        opportunity.unlink()


class OpportunityReport(models.AbstractModel):

    _name = 'report.dlg_crm.report_opportunity_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_opportunity_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.opportunity'],
            'docs': self.env['dlg_crm.opportunity'].browse(docids)
        }
