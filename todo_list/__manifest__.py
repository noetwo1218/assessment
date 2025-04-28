{
    'name': 'Todo List Management',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Manage Todo Lists and Tasks',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tags_data.xml',
        'views/todo_list_views.xml',
        # 'views/todo_task_views.xml',
    ],
    'installable': True,
    'application': True,
}
