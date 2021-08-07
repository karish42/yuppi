# Generated by Django 3.2.5 on 2021-08-07 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('EVENTS', 'EVENTS'), ('STUDIO', 'STUDIO'), ('STREET PHOTOGRAPHY', 'STREET PHOTOGRAPGY')], max_length=100)),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='pics/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='arts.post')),
            ],
        ),
    ]
