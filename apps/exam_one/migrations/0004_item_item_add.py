# Generated by Django 2.1.1 on 2018-09-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_auto_20180926_0607'),
        ('exam_one', '0003_auto_20180928_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_add',
            field=models.ManyToManyField(related_name='item_by_users', to='app_one.User'),
        ),
    ]