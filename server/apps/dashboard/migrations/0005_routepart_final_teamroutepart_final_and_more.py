# Generated by Django 4.2.1 on 2023-08-02 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0004_locationlog"),
    ]

    operations = [
        migrations.AddField(
            model_name="routepart",
            name="final",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="teamroutepart",
            name="final",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="locationlog",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="location_logs",
                to="dashboard.team",
            ),
        ),
    ]