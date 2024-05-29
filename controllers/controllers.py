from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError
import json

class MaterialController(http.Controller):

    @http.route('/api/material', type='json', auth='none', methods=['POST'])
    def create_material(self, **post):
        try:
            material = request.env['dhalig.material'].sudo().create(post)
            return {'success': True, 'data': material.read()}
        except ValidationError as e:
            return {'success': False, 'error': e.name}

    @http.route('/api/material/<int:material_id>', type='http', auth='none', methods=['GET'], csrf=False)
    def get_material(self, material_id, **kw):
        material = request.env['dhalig.material'].sudo().browse(material_id)
        if material.exists():
            material_data = {
                'id': material.id,
                'name': material.name,
                'type': material.type,
                'code': material.code,
                'buy_price': material.buy_price,
                'supplier': material.supplier_id.name if material.supplier_id else 'No Supplier'
            }
            return request.make_response(json.dumps({'success': True, 'material': material_data}), headers=[('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'success': False, 'error': 'Material not found'}), headers=[('Content-Type', 'application/json')])

    @http.route('/api/material/<int:material_id>', type='json', auth='none', methods=['PUT'])
    def update_material(self, material_id, **post):
        material = request.env['dhalig.material'].sudo().browse(material_id)
        if material:
            try:
                material.write(post)
                return {'success': True, 'data': material.read()}
            except ValidationError as e:
                return {'success': False, 'error': e.name}
        else:
            return {'success': False, 'error': 'Material not found'}

    @http.route('/api/material/<int:material_id>', type='json', auth='none', methods=['DELETE'])
    def delete_material(self, material_id, **post):
        material = request.env['dhalig.material'].sudo().browse(material_id)
        if material:
            material.unlink()
            return {'success': True, 'message': 'Material deleted successfully'}
        else:
            return {'success': False, 'error': 'Material not found'}
