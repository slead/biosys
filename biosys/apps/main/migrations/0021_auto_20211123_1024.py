# Generated by Django 3.1.3 on 2021-11-23 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_form_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='program_user', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_package',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='layout',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='data_engineers',
            field=models.ManyToManyField(blank=True, help_text='Users that can create/update projects and dataset schema within this program.', related_name='data_engineer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='attributes',
            field=models.JSONField(blank=True, help_text="Define here all specific attributes of your project in the form of json 'attribute name': 'attribute value", null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='site_data_package',
            field=models.JSONField(blank=True, help_text='Define here the attributes that all your sites will share. This allows validation when importing sites.', null=True, verbose_name='Site attributes schema'),
        ),
        migrations.AlterField(
            model_name='record',
            name='data',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='source_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='attributes',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
