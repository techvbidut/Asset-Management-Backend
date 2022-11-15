# Generated by Django 4.1.3 on 2022-11-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('per_qty_value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_on', models.DateTimeField(auto_now_add=True)),
                ('returned_on', models.DateTimeField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_resource', to='resources.resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_resource', to='accounts.user')),
            ],
        ),
    ]
