# Generated by Django 2.2.4 on 2021-07-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_DIRECCION', models.CharField(max_length=33)),
                ('ID_PREDIO', models.CharField(max_length=33)),
                ('DIRECCION_IGAC', models.CharField(max_length=33)),
                ('DIRECCION_STD', models.CharField(max_length=33)),
                ('REVISAR', models.CharField(max_length=33)),
                ('DIRECCION', models.CharField(max_length=33)),
                ('REF_CATASTRAL', models.CharField(max_length=33)),
                ('DESCRIPCION', models.CharField(max_length=33)),
                ('MAT_INMOBILIARIA', models.CharField(max_length=33)),
                ('REF_CAT_NUEVA', models.CharField(max_length=33)),
            ],
        ),
    ]