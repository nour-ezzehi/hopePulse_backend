# Generated by Django 5.0.2 on 2024-03-20 08:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_customuser_cin_customuser_profile_complete_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="cin",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="cin number must be exactly 8 digits", regex="^\\d{8}$"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="telephone_number",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be exactly 8 digits.",
                        regex="^\\d{8}$",
                    )
                ],
            ),
        ),
    ]
