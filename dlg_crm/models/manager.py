# -*- coding: utf-8 -*-

from odoo import models, fields, api
import phase, opportunity


class Manager(models.Model):
    _name = 'dlg_crm.manager'
    _description = 'Manager'

    phase_id = fields.Selection(phase.Phase.phase.id, string='Fase', required=True)
    opportunity_id = fields.Selection(opportunity.Opportunity.opportunity.name, string='Oportunidad', required=True)

    #ORM
    def f_create(self):
        manager = {
            'phase_id': 'ORM test',
            'opportunity_id': 'ORM test'
        }
        print(manager)
        self.env['dlg_crm.manager'].create(manager)

    def f_search_update(self):
        manager = self.env['dlg_crm.manager'].search([('phase_id', '=', 'ORM test')])
        print('search()', manager, manager.phase_id)

        manager_b = self.env['dlg_crm.manager'].browse([8])
        print('browse()', manager_b, manager_b.opportunity_id)

        manager.write({
            'phase_id': 'ORM test write'
        })

    def f_delete(self):
        manager = self.env['dlg_crm.manager'].browse([8])
        manager.unlink()


class ManagerReport(models.AbstractModel):

    _name = 'report.dlg_crm.report_phase_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_phase_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.manager'],
            'docs': self.env['dlg_crm.manager'].browse(docids)
        }
