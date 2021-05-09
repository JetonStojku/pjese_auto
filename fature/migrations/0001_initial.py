# Generated by Django 3.2 on 2021-05-09 13:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produkt', '0004_alter_produkt_id'),
        ('subjekte', '0002_auto_20210509_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koke_Fature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subjekte.klienti')),
                ('shites', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subjekte.shitesi')),
            ],
        ),
        migrations.CreateModel(
            name='Rrjesht_Fature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sasia', models.IntegerField()),
                ('cmimi', models.IntegerField()),
                ('zbritje', models.IntegerField()),
                ('tvsh', models.IntegerField()),
                ('fature_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fature.koke_fature')),
                ('produkt_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produkt.produkt')),
            ],
        ),
    ]
