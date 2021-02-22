# Generated by Django 3.1.7 on 2021-02-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=60)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=60)),
                ('course_duration', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
