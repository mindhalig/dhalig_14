from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'dhalig.material'
    _description = 'Material'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'id desc'

    TYPE_SELECTION = [
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ]

    code = fields.Char(
        string="Material Code",
        required=True
    )
    name = fields.Char(
        string="Material Name",
        required=True,
    )
    type = fields.Selection(
        selection=TYPE_SELECTION,
        required=True,
    )
    buy_price = fields.Float(
        string="Buy Price"
    )

    supplier_id = fields.Many2one(
        string="Supplier",
        comodel_name="res.partner",
        required=True,
        )
    
    @api.constrains('buy_price')
    def check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy price tidak boleh < 100.")