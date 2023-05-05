# Generated by Django 4.1.2 on 2023-05-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
