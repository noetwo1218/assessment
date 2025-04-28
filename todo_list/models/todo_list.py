from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(required=True, string='Title')
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], default='draft', string='Status',tracking=True)
    task_ids = fields.One2many('todo.task', 'todo_list_id', string='Tasks')
    attendee_ids = fields.One2many('todo.attendee', 'todo_list_id', string='Attendee')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date and record.end_date < record.start_date:
                raise ValidationError('End date must be after start date.')

    def action_start_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_mark_complete(self):
        for rec in self:
            if all(task.is_done for task in rec.task_ids):
                rec.state = 'complete'

    # def write(self, vals):
    #     if self.state == 'complete':
    #         raise ValidationError('Cannot edit a completed Todo List.')
    #     return super(TodoList, self).write(vals)