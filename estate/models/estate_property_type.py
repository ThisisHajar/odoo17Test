from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(string='Property Type',required = True)

    _sql_constraints = [('check_type_name', 'UNIQUE(name)', 'a type name must be unique')]


