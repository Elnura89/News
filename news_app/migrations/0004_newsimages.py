# Generated by Django 4.2.5 on 2023-09-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_news_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('newsObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.news')),
            ],
        ),
    ]