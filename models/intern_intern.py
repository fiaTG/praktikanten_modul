from odoo import models, fields, _
from odoo.exceptions import UserError

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
        template = self.env.ref(
            'praktikanten_modul.mail_template_intern_invitation',
            raise_if_not_found=False,
        )
        if not template:
            raise UserError(
                _(
                    'Die Einladungsvorlage wurde nicht gefunden. '
                    'Bitte stelle sicher, dass das Modul korrekt installiert ist.'
                )
            )

        for intern in self:
            if not intern.email:
                raise UserError(
                    _(
                        'Bitte hinterlege eine E-Mail-Adresse, bevor du eine Einladung sendest.'
                    )
                )

            lang = intern.env.context.get('lang') or intern.env.user.lang
            template.with_context(lang=lang).send_mail(intern.id, force_send=True)

        return True
