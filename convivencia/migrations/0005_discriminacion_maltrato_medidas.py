# Generated by Django 3.2.7 on 2021-09-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0004_auto_20210912_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discriminacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_discrim', models.CharField(max_length=255)),
                ('caso_vulneracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convivencia.casovulneracionderechos')),
            ],
        ),
        migrations.CreateModel(
            name='Maltrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_maltrato', models.CharField(max_length=255)),
                ('antecedentes', models.CharField(max_length=255)),
                ('caso_vulneracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convivencia.casovulneracionderechos')),
            ],
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_medida', models.CharField(max_length=255)),
                ('caso_discrim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='convivencia.discriminacion')),
                ('caso_maltrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='convivencia.maltrato')),
            ],
        ),
    ]