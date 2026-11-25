# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Genero(models.Model):
    _name = 'genero'
    _description = 'Modelo de Presupuestos'

    name = fields.Char(string="Nombre", required=True)

