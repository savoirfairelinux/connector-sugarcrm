# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'SugarCRM Connector',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Connector',
    'summary': 'SugarCRM Connector',
    'description': """
SugarCRM Connector
==================

This is a connector for SugarCRM based on the `connector`_ framework.

This connector is based on the `magento_connector`_.
Contributors
------------
* Vincent Vinet <vincent.vinet@savoirfairelinux.com>

.. _connector: https://code.launchpad.net/openerp-connector
.. _magento_connector: https://code.launchpad.net/magentoerpconnect

""",
    'depends': [
        'connector',
        'crm',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [],
    'installable': True,
}
