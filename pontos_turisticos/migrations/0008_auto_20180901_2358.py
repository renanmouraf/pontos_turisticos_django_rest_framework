# Generated by Django 2.1.1 on 2018-09-01 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0007_pontoturistico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocIdentificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='doc_identificacao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pontos_turisticos.DocIdentificacao'),
        ),
    ]