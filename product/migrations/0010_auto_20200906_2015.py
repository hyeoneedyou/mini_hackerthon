# Generated by Django 3.0.6 on 2020-09-06 20:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0009_auto_20200906_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'product')},
        ),
    ]