from odoo import models, fields

class InternIntern(models.Model):
    _name = 'intern.intern'
    _description = 'Praktikant/in'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='E-Mail')
    phone = fields.Char(string='Telefon')
    start_date = fields.Date(string='Startdatum')
    end_date = fields.Date(string='Enddatum')
    company_id = fields.Many2one('res.company', string='Unternehmen', required=True, default=lambda self: self.env.company)
    active = fields.Boolean(string='Aktiv', default=True)

    def action_send_invitation(self):
        # Platzhalter - hier kommt später die Mail/Token-Logik
        return True