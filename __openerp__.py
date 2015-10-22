#encoding=utf-8
{
    'name': "product_latest_move",
    'version': '1.0',
    'depends': ['stock'],
    'author': u"糖葫芦[39181819@qq.com]",
    'category': 'Custom',
    'description': u"""
    记录每个产品的在每个库位的最迟一次出、入库信息。
    """,
    # data files always loaded at installation
    'data': [
        'views/stock_move_record.xml',
    ],
}

