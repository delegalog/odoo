# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Phase(models.Model):
    _name = 'phase'
    _description = 'Phase'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Nombre')
    opportunity_id = fields.One2many('opportunity', 'phase', string="Oportunidad")

    #ORM
    def f_create(self):
        phase = {
            'id': 'ORM test',
            'name': 'ORM test',
            'opportunity_id': 'LEAD'
        }
        print(phase)
        self.env['phase'].create(phase)

    def f_search_update(self):
        phase = self.env['phase'].search([('name', '=', 'ORM test')])
        print('search()', phase, phase.name)

        phase_b = self.env['phase'].browse([8])
        print('browse()', phase_b, phase_b.name)

        phase.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        phase = self.env['phase'].browse([8])
        phase.unlink()


class PhaseReport(models.AbstractModel):

    _name = 'report.dlg_crm.report_phase_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_phase_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['phase'],
            'docs': self.env['phase'].browse(docids)
        }
