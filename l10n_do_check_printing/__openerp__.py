# -*- coding: utf-8 -*-
{
    'name': 'Impresion de cheques bancos Domnicanos',
    'version': '1.0',
    'author': 'Eneldo Serrata - Marcos Organizador de Negocios, SRL.',
    'website': "http://marcos.do",
    'category': 'Localization',

    'summary': 'Permite configurar desde los diarios las plantillas para impresion de chques.',
    'description': """
        Este módulo permite imprimir sus pagos en el papel de verificación pre-impreso.
        Puede configurar la salida (distribución, información trozos, etc.) en los entornos de la empresa, y gestionar el
        cheques de numeración (si utiliza cheques preimpresos sin números) en la configuración de diario.
    """,
    'depends' : ['account_check_printing'],
    'data': [
        'data/us_check_printing.xml',
        'report/print_check.xml',
        'report/print_check_bpde.xml',
        'views/res_company_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
