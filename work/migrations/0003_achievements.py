# Generated by Django 2.2.9 on 2020-04-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_work_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]