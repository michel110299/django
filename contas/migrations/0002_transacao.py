# Generated by Django 3.1.7 on 2021-03-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField(auto_now_add=True)),
                ('Descricao', models.CharField(max_length=200)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('observacoes', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.categoria')),
            ],
        ),
    ]
