# Generated by Django 4.2.8 on 2023-12-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pais",
            options={"verbose_name": "País", "verbose_name_plural": "Países"},
        ),
        migrations.AddField(
            model_name="cliente",
            name="emailid",
            field=models.CharField(default="xyz@email", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cliente",
            name="telefono",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="pais_origen_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cliente.pais",
                verbose_name="País de origen",
            ),
        ),
    ]