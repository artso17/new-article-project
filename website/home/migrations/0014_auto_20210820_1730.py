# Generated by Django 3.2 on 2021-08-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='snippets',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/artikel'),
        ),
    ]
