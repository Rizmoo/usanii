# Generated by Django 2.0 on 2017-12-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='file',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]