# Generated by Django 4.0.6 on 2022-07-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employer_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='employee.employer'),
        ),
    ]
