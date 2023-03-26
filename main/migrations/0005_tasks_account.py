# Generated by Django 4.1.7 on 2023-03-25 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_tasks_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
