# Generated by Django 3.2 on 2022-08-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mksd', '0006_post_snippets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='click the link above.', max_length=255),
        ),
    ]
