# Generated by Django 5.0.7 on 2024-07-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imtxonapp', '0006_murtojat_alter_companya_tarixi_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='murtojat',
            name='kompaniy_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
