# Generated by Django 4.2.4 on 2023-08-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_fix_register"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
