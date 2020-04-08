# Generated by Django 3.0.5 on 2020-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title_jop', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='doctor_image/')),
                ('bio', models.TextField()),
                ('facbook_url', models.URLField()),
                ('pinterest_url', models.URLField()),
                ('linkedin_url', models.URLField()),
                ('twitter_url', models.URLField()),
            ],
        ),
    ]