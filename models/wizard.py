from openerp import models, fields, api, exceptions, _


class TodoWizard(models.TransientModel):
    _name = "product_latest_move.wizard"

    