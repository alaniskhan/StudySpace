# Generated by Django 4.0.4 on 2022-10-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_material_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]
