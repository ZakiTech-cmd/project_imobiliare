# Generated by Django 4.1.1 on 2022-09-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imobiliare', '0002_alter_announce_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announce',
            options={'ordering': ['-last_update', '-publish_date']},
        ),
        migrations.AddField(
            model_name='announce',
            name='phone_number',
            field=models.CharField(default=40737101220, max_length=20),
            preserve_default=False,
        ),
    ]
