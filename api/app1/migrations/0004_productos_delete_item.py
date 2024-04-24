# Generated by Django 5.0.4 on 2024-04-24 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_item_delete_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
