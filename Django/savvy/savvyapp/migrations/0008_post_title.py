# Generated by Django 5.0.6 on 2024-07-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savvyapp', '0007_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]