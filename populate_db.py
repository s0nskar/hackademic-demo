import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hackademic.settings')

import django
django.setup()

from django.contrib.auth.models import User, Group, Permission
from hackademic.models import Article

def add_group(name, *permissions):
    g = Group.objects.get_or_create(name=name)[0]
    g.permissions.clear()
    for permission in permissions:
        try:
            p = Permission.objects.get(codename=permission)
            g.permissions.add(p)
        except Exception as e:
            print permission
    g.save()
    return g

def add_user(username, password, email, group):
    u = User.objects.get_or_create(username=username,
                                email=email)[0]
    u.set_password(password)
    g = Group.objects.get(name=group)
    u.groups.add(g)
    u.save()

def populate():
    add_group('Student')
    add_group('Teacher', 
            'add_article',
            'change_article',
            'delete_article',
        )
    add_group('Admin',
            'add_article',
            'change_article',
            'delete_article',
        )

    add_user('a', '1234', 'a@a.a', 'Student')
    add_user('b', '1234', 'b@b.b', 'Teacher')
    add_user('c', '1234', 'c@c.c', 'Admin')

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()