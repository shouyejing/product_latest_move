from openerp import models, fields, api, exceptions, _


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.one
    def action_done(self):
        super(StockMove, self).action_done()
        self.update_product_latest_move()

    @api.one
    def update_product_latest_move(self):
        source_loc_out_rec = self.product_id.stock_move_record_ids.filtered(
            lambda r: r.location_id == self.location_id and r.type == "out")
        if source_loc_out_rec:
            source_loc_out_rec.ensure_one()
            source_loc_out_rec.datetime = self.date
        else:
            vals = dict()
            vals["product_id"] = self.product_id.id
            vals["type"] = "out"
            vals["location_id"] = self.location_id.id
            vals["datetime"] = self.date
            self.env["product_latest_move.stock_move_record"].create(vals)
        dest_loc_in_rec = self.product_id.stock_move_record_ids.filtered(
            lambda r: r.location_id == self.location_dest_id and r.type == "in")
        if dest_loc_in_rec:
            dest_loc_in_rec.ensure_one()
            dest_loc_in_rec.datetime = self.date
        else:
            vals = dict()
            vals["product_id"] = self.product_id.id
            vals["type"] = "in"
            vals["location_id"] = self.location_dest_id.id
            vals["datetime"] = self.date
            self.env["product_latest_move.stock_move_record"].create(vals)
