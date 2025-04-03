{
    'name': 'Work Order Priority Sync',
    'version': '1.0',
    'author': 'KLZ Deportes',
    'license': 'LGPL-3',
    'category': 'Manufacturing',
    'summary': 'Sincroniza la prioridad entre órdenes de producción y órdenes de trabajo.',
    'description': """
        Este módulo agrega un campo de prioridad (estrella ⭐) visible y no editable a las órdenes de trabajo.
        Se sincroniza automáticamente con la prioridad de la orden de producción asociada.
        La prioridad es visible desde la vista lista de órdenes de trabajo.
    """,
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_workorder_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['icon.png'],
}
