# Generated by Django 4.0.4 on 2023-03-04 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_department_cordinator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='hoduser',
            name='address',
            field=models.TextField(default='ogbomosho'),
        ),
        migrations.AddField(
            model_name='hoduser',
            name='phone',
            field=models.PositiveBigIntegerField(default=8011223344),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='phone',
            field=models.PositiveBigIntegerField(default=8011223344),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='address',
            field=models.TextField(default='ogbomosho'),
        ),
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='ogbomosho')),
                ('phone', models.PositiveBigIntegerField(default=8011223344)),
                ('admission_year', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.department')),
                ('staff_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]