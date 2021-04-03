# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class OpportunityController(http.Controller):

    @http.route('/api/opportunity', auth='public', method=['GET'], csrf=False)
    def get_opportunity(self, **kw):
        try:
            opportunity = http.request.env['dlg_crm.opportunity'].sudo().search_read([], ['id', 'name', 'customer',
                                                                                          'notes', 'done', 'image',
                                                                                          'phase', 'done'])
            res = json.dumps(opportunity, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class PhaseController(http.Controller):

    @http.route('/api/phase', auth='public', method=['GET'], csrf=False)
    def get_phase(self, **kw):
        try:
            phase = http.request.env['dlg_crm.phase'].sudo().search_read([], ['id', 'name', 'opportunity'])
            res = json.dumps(phase, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class ManagerController(http.Controller):

    @http.route('/api/manager', auth='public', method=['GET'], csrf=False)
    def get_manager(self, **kw):
        try:
            manager = http.request.env['dlg_crm.manager'].sudo().search_read([], ['phase_id', 'opportunity_id'])
            res = json.dumps(manager, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
