from odoo import models, fields, api
class Heroes(models.Model):
    _name = 'heroes.heroes'
    _description = 'Superhéroes de la empresa'
    _rec_name = 'nombre'
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellido')
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo')
    nombre_superhero = fields.Char(string='Nombre Superheroe')
    trabajador_parecido = fields.One2one('res.users',string='Trabajador Parecido', ondelete='set null')

    @api.depends('nombre','apellidos','nombre_completo')
    def _compute_nombre_completo(self):
        for record in self:
            heroes.nombre_completo=str(record.nombre)+' '+record.apellidos