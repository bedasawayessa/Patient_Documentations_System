# Generated by Django 4.2.7 on 2024-05-20 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]