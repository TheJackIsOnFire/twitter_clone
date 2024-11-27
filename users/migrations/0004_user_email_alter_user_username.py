# Generated by Django 5.1.3 on 2024-11-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default="xxx@email.com", max_length=254, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="@username", max_length=254, unique=True),
        ),
    ]
