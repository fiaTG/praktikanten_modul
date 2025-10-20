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
        'hr_timesheet',
        'portal',
        # 'sign',  # optional, Enterprise only
    ],
    'data': [
        # Security
        'security/intern_security.xml',
        'security/ir.model.access.csv',
        # Data
        # 'data/demo_data.xml',
        # Views
        'views/intern_intern_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
