# Generated by Django 4.0.3 on 2022-05-13 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('year', models.SmallIntegerField()),
                ('actors', models.ManyToManyField(related_name='movies_cast', to='movielist.person')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_directed', to='movielist.person')),
            ],
        ),
    ]
