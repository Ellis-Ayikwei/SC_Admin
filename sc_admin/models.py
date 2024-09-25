#!/usr/bin/env python3
from django.db import migrations, models
from django.utils import timezone

def set_default_created_at(apps, schema_editor):
    User = apps.get_model('admin_01', 'Users')
    User.objects.filter(created_at__isnull=True).update(created_at=timezone.now())

class Migration(migrations.Migration):

    dependencies = [
        # Add your migration dependencies here
    ]

    operations = [
        migrations.RunPython(set_default_created_at),
    ]
