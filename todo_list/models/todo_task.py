from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char(required=True)
    description = fields.Text()
    is_done = fields.Boolean(string='Is Complete')
    todo_list_id = fields.Many2one('todo.list', string='Todo List')
