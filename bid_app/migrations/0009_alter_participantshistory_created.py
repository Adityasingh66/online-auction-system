# Generated by Django 4.0.4 on 2022-05-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_app', '0008_participantshistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantshistory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
