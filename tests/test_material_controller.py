from odoo.tests.common import HttpCase
import json

class TestMaterialController(HttpCase):
    
    def setUp(self):
        super(TestMaterialController, self).setUp()
        self.Material = self.env['dhalig.material']
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})

    def test_create_material(self):
        url = 'http://localhost:8014/api/material'  
        data = {
            'code': 'MAT02',
            'name': 'Material Test 2',
            'type': 'fabric',
            'buy_price': 250,
            'supplier_id': self.partner.id
        }
        headers = {'Content-Type': 'application/json'}
        response = self.opener.post(url, data=json.dumps(data), headers=headers)
        response_data = json.loads(response.content.decode())
        self.assertTrue(response_data.get('success'), 'Material should be created successfully')

    def test_delete_material(self):
        material = self.Material.create({
            'code': 'MAT03',
            'name': 'Material Test 3',
            'type': 'fabric',
            'buy_price': 300,
            'supplier_id': self.partner.id
        })
        url = 'http://localhost:8014/api/material/{}'.format(material.id)  
        headers = {'Content-Type': 'application/json'}
        response = self.opener.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200, 'Material should be deleted successfully')

    def test_get_material(self):
        material = self.Material.create({
            'code': 'MAT04',
            'name': 'Material Test 4',
            'type': 'fabric',
            'buy_price': 350,
            'supplier_id': self.partner.id
        })
        url = 'http://localhost:8014/api/material/{}'.format(material.id) 
        headers = {'Content-Type': 'application/json'}
        response = self.opener.get(url, headers=headers)
        response_data = json.loads(response.content.decode())
        self.assertEqual(response_data['code'], 'MAT04', 'Material code should be MAT04')

    def test_update_material(self):
        material = self.Material.create({
            'code': 'MAT05',
            'name': 'Material Test 5',
            'type': 'fabric',
            'buy_price': 400,
            'supplier_id': self.partner.id
        })
        url = 'http://localhost:8014/api/material/{}'.format(material.id) 
        update_data = {
            'name': 'Updated Material Test 5',
            'buy_price': 450
        }
        headers = {'Content-Type': 'application/json'}
        response = self.opener.put(url, data=json.dumps(update_data), headers=headers)
        self.assertEqual(response.status_code, 200, 'Material should be updated successfully')