# Generated by Django 3.2.4 on 2021-07-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_auto_20210722_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='uid_id',
            new_name='uid',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]