# coding: utf-8
###########################################################################
#    Copyright (C) Eder Ortiz (eder.o@icloud.com)
#    All Rights Reserved
# Credits######################################################
#    Coded by:   Eder Ortiz eder.o@icloud.com
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from openerp.osv import fields, osv

class product_template(osv.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    _columns = {
            'related_products': fields.many2many('product.template', 'rel_related_product', 'product_id', 'product_template_id', string="Related Products"),
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
