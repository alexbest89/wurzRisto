# Generated by Django 3.0.3 on 2020-02-28 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tavoli', '0010_auto_20200228_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spec_scon',
            name='id_scon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tavoli.Scontrino'),
        ),
    ]
