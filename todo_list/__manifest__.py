{
    'name': 'Todo List Management',
    "version": "18.0.0.0.1",
    'category': 'Productivity',
    'summary': 'Manage Todo Lists and Tasks',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tags_data.xml',
        'views/todo_list_views.xml',
    ],
    'installable': True,
    'application': True,
}
