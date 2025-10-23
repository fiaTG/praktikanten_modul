# -*- coding: utf-8 -*-
{
    'name': 'Praktikantenmodul',
    'version': '1.0.0',
    'summary': 'Verwaltung von Praktikant:innen, Aufgaben, Zeiten und Wochenberichten',
    'description': """
Odoo-Modul für Ausbildungsbetriebe und Unternehmen zur effizienten Verwaltung von Praktikant:innen.
Enthält Funktionen für Aufgabenmanagement, Zeiterfassung, Wochenberichte und Portalzugang.
""",
    'author': 'fiaTG',
    'website': 'https://github.com/fiaTG/praktikanten_modul',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
        'project',
        'hr',
        'hr_timesheet',
        'portal',
        'mail',
        # 'sign',  # optional, Enterprise only
    ],
    'data': [
        'security/intern_security.xml',
        'security/ir.model.access.csv',
        'views/intern_intern_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}