# Generated by Django 5.2.1 on 2025-07-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
