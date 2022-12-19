{
    'name': 'Tolerance',
    'version': '15.0.1.0.0',
    'sequence': 100,
    'depends': ['base',
                'sale',
                'contacts',
                'stock',
                'purchase',
                ],
    'data': [
            'security/ir.model.access.csv',
            'view/tolerance.xml',
            'view/purchase_tolerance.xml',
            'view/stock_tolerance.xml',
            'wizard/wizard.xml',
                ],
    'license': 'LGPL-3',
}