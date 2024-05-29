from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterialModel(TransactionCase):
    def setUp(self):
        super(TestMaterialModel, self).setUp()
        # Setup for test, creating needed records
        self.Supplier = self.env['res.partner'].create({'name': 'Test Supplier'})

    def test_01_check_buy_price_constraint(self):
        """ Test buy_price must not be less than 100 """
        with self.assertRaises(ValidationError, msg="Buy price tidak boleh < 100."):
            # This should raise a ValidationError because the buy price is less than 100
            self.env['dhalig.material'].create({
                'name': 'Low Price Material',
                'code': 'LOW100',
                'type': 'fabric',
                'buy_price': 50,  # Invalid buy price
                'supplier_id': self.Supplier.id
            })

    def test_02_create_valid_material(self):
        """ Test creating a valid material with buy_price >= 100 """
        material = self.env['dhalig.material'].create({
            'name': 'Valid Material',
            'code': 'VAL200',
            'type': 'jeans',
            'buy_price': 200,  # Valid buy price
            'supplier_id': self.Supplier.id
        })
        self.assertEqual(material.buy_price, 200, "The buy price should be set correctly.")
