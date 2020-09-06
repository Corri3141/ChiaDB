# Generated by Django 3.0.3 on 2020-09-06 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chia', '0002_auto_20200906_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='comprador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chia.Cliente'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fecha_de_venta',
            field=models.DateField(blank=True, null=True),
        ),
    ]
