# Generated by Django 3.2.12 on 2022-04-15 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0003_auto_20220415_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies_app.departments'),
        ),
    ]
