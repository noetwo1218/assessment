from odoo import models, fields


class TodoAttendee(models.Model):
    _name = 'todo.attendee'
    _description = 'Todo Attendee'

    user_id = fields.Many2one('res.users', string='Attendee')
    todo_list_id = fields.Many2one('todo.list', string='Todo List')