# Generated by Django 4.2.10 on 2024-03-20 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 10, 10, 13, 237552, tzinfo=datetime.timezone.utc)),
        ),
    ]
