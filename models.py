# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class LibraryBooks(models.Model):
    _name = 'library.books'
    _description = 'Books Records'
    _rec_name = 'title'

    title = fields.Char(string="Title", required=True)
    description = fields.Text()
    about = fields.Text()
    image = fields.Binary(string="Image", readonly=False)
    author = fields.Char(string="Author", required=True)
    publisher = fields.Char(string="Publisher")
    unit_price = fields.Float()
    quantity = fields.Float()
    price = fields.Float(string="Price", compute='_onchange_price', store=True)
    edition = fields.Char(string="Book Edition")
    name_seq = fields.Char(string='Books Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    librarian_id = fields.Many2one('res.users', ondelete='set null', string="Librarian", index=True)
    issued_books_ids = fields.One2many('library.issued_books', 'id', string="Issued Book ID")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('library.books.sequence') or _('New')
        result = super(LibraryBooks, self).create(vals)
        return result

    @api.depends('unit_price', 'quantity')
    def _onchange_price(self):
        self.price = self.unit_price * self.quantity


class IssuedBooks(models.Model):
    _name = 'library.issued_books'
    _description = 'Issued Books Records'
    _rec_name = 'title'

    title = fields.Char(string='Book Title', required=True)
    author = fields.Char(string="Author", required=True)
    member_name = fields.Char(string='Member name')
    member_id = fields.Char(string='Member ID', required=True)
    issue_date = fields.Date(string='Issued Date', default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
    book_status = fields.Boolean(string='Book Returned', default=False)
    name_sequence = fields.Char(string='Issued Book Reference', required=True, copy=False, readonly=True,
                                index=True, default=lambda self: _('New'))

    asst_librarian_id = fields.Many2one('res.partner', string="Assistant Librarian")
    book_id = fields.Many2one('library.books', ondelete='cascade', string="id", required=True)

    state = fields.Selection([
        ('available', "Available"),
        ('issued', "Issued"),
        ('returned', "Returned"), ], default='available')

    @api.model
    def action_available(self):
        self.state = 'available'

    @api.model
    def action_issued(self):
        self.state = 'issued'

    @api.model
    def action_returned(self):
        self.state = 'returned'

    @api.model
    def unlink(self):
        print('**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$123')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xyss')
        return models.Model.unlink(self)

    @api.constrains('librarian_id', 'asst_librarian_id')
    def _check_librarian_not_in_asst_librarian(self):
        for r in self:
            if r.librarian_id in r.asst_librarian_id:
                raise exceptions.ValidationError("An assistant librarian can't be a librarian")

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code('library.issued.sequence') or _('New')
        result = super(IssuedBooks, self).create(vals)
        return result


class LibraryVendor(models.Model):
    _name = 'library.vendors'
    _description = 'Books Vendors'

    vendor_title = fields.Char(string='Vendor Title')
    phone_number = fields.Integer(string='Phone Number')
    mobile_number = fields.Integer(string='Mobile Number')
    email_address = fields.Integer(string='Email Address')


class LibraryMember(models.Model):
    _name = 'library.members'
    _description = 'Members Details'
    _rec_name = 'members_name'

    members_name = fields.Char(string='Members Name', required=True)
    image = fields.Binary(string="Image", readonly=False)
    date_from = fields.Date(string='From', readonly=True)
    date_to = fields.Date(string='To', readonly=True)
    date_cancel = fields.Date(string='Cancel date')
    date_joined = fields.Date(string='Join Date', help="Date on which member has joined the membership")
    member_price = fields.Float(string='Membership Fee', digits='Product Price', required=True,
                                help='Amount for the membership')
    no_book_issued = fields.Integer(string='no BookIssued')
    max_book_limit = fields.Integer(string='Max Book Limit')
    address = fields.Integer(string='Address')
    phone_number = fields.Char(string='Phone Number')
    email_address = fields.Char(string='Email Address')
    fines_owed = fields.Integer(string='Fines Owed')
    member_sequence = fields.Char(string='Member Reference', required=True, copy=False, readonly=True,
                                  index=True, default=lambda self: _('New'))
    type = fields.Selection([
        ('free membership', "Free Membership"),
        ('monthly membership', "Monthly Membership"),
        ('yearly membership', "Yearly Membership"), ], default='free membership')

    def action_free_membership(self):
        self.type = 'free membership'

    def action_monthly_membership(self):
        self.type = 'monthly membership'

    def action_yearly_membership(self):
        self.type = 'yearly membership'

    @api.model
    def create(self, vals):
        if vals.get('member_sequence', _('New')) == _('New'):
            vals['member_sequence'] = self.env['ir.sequence'].next_by_code('library.members.sequence') or _('New')
        result = super(LibraryMember, self).create(vals)
        return result

