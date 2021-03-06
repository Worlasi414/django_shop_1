# Generated by Django 2.2 on 2020-01-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test_product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('К', 'Комплект ключей'), ('Ш', 'Поштучно')], max_length=30),
        ),
    ]
