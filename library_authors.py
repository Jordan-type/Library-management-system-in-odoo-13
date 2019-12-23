# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class LibraryAuthors(models.Model):
    _name = 'library.authors'
    _description = 'Authors Records'
    _rec_name = 'author_title'

    author_title = fields.Char(string='Authors Title')
    author_name = fields.Char(string='Author Name')
    author_image = fields.Binary(string='Author Image')
    awards = fields.Binary(string='Awards')
    books_number = fields.Integer(string='Number of Books')
    birth_date = fields.Date(string='Date of Birth')
    death_date = fields.Date(string='Date of Death')
    biography = fields.Text('Biography')
    note = fields.Text('Notes')
    author_sequence = fields.Char(string='Author Reference', required=True, copy=False, readonly=True,
                                  index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('author_sequence', _('New')) == _('New'):
            vals['author_sequence'] = self.env['ir.sequence'].next_by_code('library.authors.sequence') or _('New')
        result = super(LibraryAuthors, self).create(vals)
        return result


