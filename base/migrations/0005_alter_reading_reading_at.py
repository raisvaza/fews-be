# Generated by Django 4.2.6 on 2023-10-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_auto_20231018_1957"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reading",
            name="reading_at",
            field=models.DateTimeField(),
        ),
    ]