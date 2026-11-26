# -*- coding:utf-8 -*-

{
    'name': 'Modulo de Peliculas',
    'version': '1.0',
    'depends': [
        'contacts',
        'mail',
    ],
    'author': 'Cristian Vargas',
    'category': 'Peliculas',
    'website': 'https://www.google.com',
    'summary': 'Modulo de pesupuestos para Peliculas',
    'description': """
    Modulo para hacer presupuestos de peliculas
    """,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/categoria.xml',
        'data/secuencia.xml',
        'wizard/update_wizard_views.xml',
        'report/reporte_peliculas.xml',
        'views/presupuesto_views.xml',
        'views/menu.xml',
    ],
}