# Generated by Django 3.0.9 on 2023-01-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('serial', models.CharField(max_length=5)),
                ('model', models.CharField(max_length=2)),
                ('version', models.CharField(max_length=2)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
