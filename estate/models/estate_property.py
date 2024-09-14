from email.policy import default

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

from odoo.exceptions import UserError, ValidationError

from odoo import fields, models
from datetime import datetime, timedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string='Name',required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False,default=datetime.today()+timedelta(days=90))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True, copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades = fields.Integer()
    garage=fields.Boolean()
    garden = fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(selection=[("north", "North"),("south", "South"),("east", "East"),("west", "West"),],)
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
                           required=True,
                           copy=False,
                           )

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson = fields.Many2one("res.users", string="Salesman")
    buyer = fields.Many2one("res.partner", string="Buyer")



