# Generated by Django 2.2.2 on 2019-06-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('test_app', '0003_auto_20190626_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='baz',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contenttypes.ContentType'),
        ),
    ]
