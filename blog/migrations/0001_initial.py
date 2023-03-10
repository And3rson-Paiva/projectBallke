# Generated by Django 4.1.7 on 2023-03-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("titulo", models.CharField(max_length=200, verbose_name="Título")),
                ("conteudo", models.TextField(verbose_name="Conteudo")),
                ("autor", models.CharField(max_length=200, verbose_name="Autor")),
                (
                    "data_publicacao",
                    models.DateField(
                        auto_now_add=True, verbose_name="Data de Publicação"
                    ),
                ),
            ],
        ),
    ]
