# Generated by Django 4.0.4 on 2022-04-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_category_remove_post_excerpt_post_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='cites',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
