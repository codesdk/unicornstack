# Generated by Django 4.0 on 2022-01-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Assets',
                'ordering': ['name', 'created_at'],
            },
        ),
    ]