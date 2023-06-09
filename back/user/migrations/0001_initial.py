# Generated by Django 4.1.7 on 2023-04-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('d_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('andress', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='members_profile')),
            ],
        ),
    ]
