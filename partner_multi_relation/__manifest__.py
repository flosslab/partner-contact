# -*- coding: utf-8 -*-
# © 2013-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Partner relations",
    "version": "11.0.1.0.1",
    "author": "Therp BV,Camptocamp,Odoo Community Association (OCA)",
    "complexity": "normal",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "depends": [
        'crm'
    ],
    "demo": [
        "data/demo.xml",
    ],
    "data": [
        "security/group.xml",
        "security/ir.model.access.csv",
        "views/res_partner_relation_all.xml",
        'views/res_partner.xml',
        'views/res_partner_relation_type.xml',
        'views/menu.xml',
    ],
    "auto_install": False,
    "installable": True,
}
