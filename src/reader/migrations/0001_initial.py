# Generated by Django 4.0.7 on 2022-08-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('text', models.TextField(verbose_name='Texto')),
                ('details', models.TextField(verbose_name='Detalhes')),
                ('folder', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
    ]