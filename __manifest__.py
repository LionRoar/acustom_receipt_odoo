{
    'name': "acustom_receipt",
    'depends': ['base'],
    'category': 'Marketing',
    'application': True,
    'version': '1.0',

    'data': [
       
     ],
    'assets': {
        'point_of_sale._assets_pos': [
            'acustom_receipt/static/src/xml/**/*',
            'acustom_receipt/static/src/scss/**/*'
        ],
    },
}