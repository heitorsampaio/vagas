# Generated by Django 3.1.1 on 2020-10-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, help_text='Fullname of the Client', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(help_text='Valid CPF of the Client', max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Email of the Client', max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]