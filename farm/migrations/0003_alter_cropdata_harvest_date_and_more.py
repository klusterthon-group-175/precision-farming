# Generated by Django 4.2.7 on 2023-11-23 09:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0002_rename_crop_cropdata_rename_farm_farmdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropdata',
            name='harvest_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='farmdata',
            unique_together={('name', 'owner')},
        ),
    ]