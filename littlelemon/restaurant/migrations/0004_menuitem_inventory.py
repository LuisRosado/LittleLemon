# Generated by Django 5.1.2 on 2024-11-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_menuitem_inventory_alter_booking_no_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.SmallIntegerField(default=0),
        ),
    ]
