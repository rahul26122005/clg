# Generated by Django 3.2.25 on 2024-06-16 05:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('roll_number', models.CharField(max_length=10, null=True)),
                ('student_class', models.CharField(max_length=10, null=True)),
                ('section', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('od', 'On Duty')], max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
    ]
