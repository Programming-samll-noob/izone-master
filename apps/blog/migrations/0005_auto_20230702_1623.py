# Generated by Django 2.2.28 on 2023-07-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230702_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendlink',
            name='not_show_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='禁用原因'),
        ),
        migrations.AlterField(
            model_name='friendlink',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否展示'),
        ),
    ]
