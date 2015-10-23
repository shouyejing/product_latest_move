from openerp import models, fields, api, exceptions, _


class StockMoveRecord(models.Model):
    _name = "product_latest_move.stock_move_record"

    product_id = fields.Many2one("product.product")
    location_id = fields.Many2one("stock.location")
    datetime = fields.Datetime()
    type = fields.Selection([("in", "In"), ("out", "Out")])


class Product(models.Model):
    _inherit = "product.product"

    stock_move_record_ids = fields.One2many("product_latest_move.stock_move_record", "product_id")
