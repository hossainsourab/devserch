# Generated by Django 4.0 on 2021-12-31 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
