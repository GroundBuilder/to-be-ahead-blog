# Generated by Django 3.2.18 on 2023-04-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everydayblog', '0007_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'BOL'), (1, 'EDC'), (2, 'Outher')], default=2),
        ),
    ]