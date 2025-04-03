{
    'name': 'Work Order Priority Sync',
    'version': '1.0',
    'author': 'KLZ Deportes',
    'license': 'LGPL-3',
    'category': 'Manufacturing',
    'summary': 'Muestra la prioridad en las órdenes de trabajo sincronizada con la orden de producción',
    'description': 'Agrega un campo de prioridad visible (no editable) en las órdenes de trabajo, que refleja la prioridad de la orden de producción.',
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_workorder_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
