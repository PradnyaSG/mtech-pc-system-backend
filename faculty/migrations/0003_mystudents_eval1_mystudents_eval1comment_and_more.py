# Generated by Django 5.0.3 on 2024-03-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_mystudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystudents',
            name='eval1',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='eval1comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='eval2',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='eval2comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='eval3',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='eval3comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='projectname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report1',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report1acceptancestatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report1comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report2',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report2acceptancestatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report2comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report3',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report3acceptancestatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mystudents',
            name='report3comment',
            field=models.CharField(default='', max_length=100),
        ),
    ]
