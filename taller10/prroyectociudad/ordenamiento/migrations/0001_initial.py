# Generated by Django 3.2.4 on 2021-06-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('1', 'urbana'), ('2', 'rural')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Las Parroquias',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_viviendas', models.IntegerField()),
                ('numero_parques', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=30)),
                ('numero_edificios', models.IntegerField()),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losbarrios', to='ordenamiento.parroquia')),
            ],
            options={
                'verbose_name_plural': 'Los Barrios',
            },
        ),
    ]
