# Generated by Django 4.1.5 on 2023-01-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consuarq', '0004_alter_pessoa_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='file',
            field=models.FileField(upload_to='consuarq/media'),
        ),
    ]