# Generated by Django 4.2.9 on 2024-04-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="number",
            field=models.IntegerField(
                blank=True, null=True, unique=True, verbose_name="number"
            ),
        ),
    ]
