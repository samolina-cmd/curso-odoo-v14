# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Presupuesto(models.Model):
    _name = 'presupuesto'
    _inherit = ['image.mixin']
    _description = 'Modelo de Presupuestos'

    name = fields.Char(string="Película", required=True)

    clasificacion = fields.Selection(
        selection=[
            ("G", "G"),          # Público general
            ("PG", "PG"),        # Se recomienda la compañía de un adulto
            ("PG-13", "PG-13"),  # Mayores de 13
            ("R", "R"),          # En compañía de un adulto obligatorio
            ("NC-17", "NC-17"),  # Mayores de 18
        ],
        string="Clasificación",
        help="G: Público general / PG: Se recomienda compañía de un adulto / PG-13: Mayores de 13 / R: En compañía de un adulto obligatorio / NC-17: Mayores de 18"
    )

    fch_estreno = fields.Date(string="Fecha de Estreno")
    puntuacion = fields.Integer(string="Puntuación", copy=False)
    puntuacion2 = fields.Integer(string="Puntuación 2", related="puntuacion", readonly=False)
    active = fields.Boolean(string="Activo", default=True)

    director_id = fields.Many2one(
        comodel_name='res.partner',
        string="Director"
    )
    categoria_director_id= fields.Many2one(
        comodel_name='res.partner.category',
        string='Categoría Director'
    )

    genero_ids = fields.Many2many(
        comodel_name='genero',
        string="Géneros"
    )

    # CAMPOS NUEVOS CORREGIDOS (Con la sangría correcta)
    vista_general = fields.Text(string='Descripción')
    link_trailer = fields.Char(string='Trailer')
    es_libro = fields.Boolean(string='Versión libro')
    libro = fields.Binary(string='Libro')
    libro_filename = fields.Char(string='Nombre del libro')


class Genero(models.Model):
    _name = 'genero'
    _description = 'Modelo de Géneros de Películas'

    name = fields.Char(string="Nombre del Género", required=True)
