# Generated by Django 4.2.6 on 2023-10-18 12:57

from django.db import migrations
from base.models import Pos


def create_Pos_dummy_data(apps, schema_editor):
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-0.9914911213345805, longitude=116.72983422740246, tipe="CurahHujan")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-0.9760009659068754, longitude=116.73575654470451, tipe="CurahHujan")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-1.0063375736282987, longitude=116.71610131768118, tipe="CurahHujan")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-0.9914911213345805, longitude=116.7359711214169, tipe="CurahHujan")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-1.0230719330191822, longitude=116.69365659328528, tipe="CurahHujan")

    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-1.022900298932718, longitude=116.710565238586, tipe="DugaAir")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-1.0025616038170988, longitude=116.74318089909023, tipe="DugaAir")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-0.9855696856040823, longitude=116.7456699889708, tipe="DugaAir")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-0.969779138409185, longitude=116.75279393587041, tipe="DugaAir")
    Pos.objects.create(nama = "Pos Duga Air #1", latitude=-1.0357728245197677, longitude=116.69254079460548, tipe="DugaAir")


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_pos_updated_at"),
    ]

    operations = [
        migrations.RunPython(create_Pos_dummy_data)
    ]
