# Generated by Django 2.1.15 on 2020-06-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API_Name', models.CharField(max_length=200)),
                ('API_Link', models.CharField(max_length=200)),
                ('API_Des', models.CharField(max_length=200)),
                ('API_Auth', models.CharField(max_length=200)),
                ('API_HTTPS', models.CharField(max_length=200)),
                ('API_CORS', models.CharField(max_length=200)),
            ],
        ),
    ]
