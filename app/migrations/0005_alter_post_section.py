# Generated by Django 4.0.3 on 2022-03-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_post_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('Popular', 'Polular'), ('Recent', 'Recent'), ('Editors_Pick', 'Editors_Pick'), ('Trending', 'Trending'), ('Inspiration', 'Inspiration'), ('Latest_Posts', 'Latest Posts')], max_length=200),
        ),
    ]
