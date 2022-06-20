# Generated by Django 4.0.4 on 2022-06-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.TextField()),
                ('who_wrote_it', models.CharField(choices=[], max_length=250, null=True)),
                ('relation', models.CharField(choices=[], max_length=250, null=True)),
                ('relation_elaboration', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='relation_elaboration',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='who_wrote_it',
        ),
    ]
