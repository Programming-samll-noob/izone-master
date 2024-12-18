# Generated by Django 2.2.28 on 2024-01-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_feedhub'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedhub',
            options={'ordering': ['sort_order'], 'verbose_name': 'Feed Hub', 'verbose_name_plural': 'Feed Hub'},
        ),
        migrations.AddField(
            model_name='feedhub',
            name='sort_order',
            field=models.IntegerField(default=99, help_text='作为显示的时候的顺序', verbose_name='排序'),
        ),
    ]
