# Generated by Django 2.2.9 on 2020-05-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tech', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
