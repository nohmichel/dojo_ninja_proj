# Generated by Django 2.2 on 2021-02-18 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0004_auto_20210218_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
        ),
    ]
