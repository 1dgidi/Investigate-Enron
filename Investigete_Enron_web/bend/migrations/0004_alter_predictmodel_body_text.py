# Generated by Django 4.0.4 on 2022-06-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bend', '0003_alter_predictmodel_body_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictmodel',
            name='body_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]