# Generated by Django 3.1.7 on 2021-05-06 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
        ('produkt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='marka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auto.marka'),
        ),
    ]
