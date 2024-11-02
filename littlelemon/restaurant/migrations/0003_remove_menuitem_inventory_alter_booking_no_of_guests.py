# Generated by Django 5.1.2 on 2024-11-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_menu_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='inventory',
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(),
        ),
    ]