# Generated by Django 4.2.8 on 2023-12-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('roll_number', 'class_level')},
        ),
    ]
