# Generated by Django 4.2.9 on 2024-01-19 14:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductoCategoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                (
                    "descripcion",
                    models.TextField(blank=True, null=True, verbose_name="descripción"),
                ),
            ],
            options={
                "verbose_name": "categpría de producto",
                "verbose_name_plural": "categprías de Productos",
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("unidad_medida", models.CharField(max_length=100)),
                ("cantidad", models.FloatField()),
                ("precio", models.FloatField()),
                (
                    "descripcion",
                    models.TextField(blank=True, null=True, verbose_name="descripción"),
                ),
                (
                    "fecha_actualizacion",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        null=True,
                        verbose_name="fecha de actualización",
                    ),
                ),
                (
                    "categoria_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="producto.productocategoria",
                        verbose_name="categpría",
                    ),
                ),
            ],
            options={"verbose_name": "producto", "verbose_name_plural": "productos",},
        ),
    ]
