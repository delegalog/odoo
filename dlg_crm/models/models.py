# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Visit(models.Model):
    _name = 'dlg_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('C', 'Call'), ('P', 'Presencial'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done = not self.done

    #ORM
    def f_create(self):
        visit = {
            'name': 'ORM test',
            'notes': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(visit)
        self.env['dlg_crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['dlg_crm.visit'].search([('name', '=', 'ORM test')])
        print('search()', visit, visit.name)

        visit_b = self.env['dlg_crm.visit'].browse([8])
        print('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['dlg_crm.visit'].browse([8])
        visit.unlink()


class VisitReport(models.AbstractModel):

    _name='report.dlg_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.visit'],
            'docs': self.env['dlg_crm.visit'].browse(docids)
        }


class CustomSaleOrder(models.Model):

    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur')], string='Zona comercial')