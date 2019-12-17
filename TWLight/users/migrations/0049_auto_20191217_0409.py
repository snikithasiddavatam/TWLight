# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0048_reset_tou_for_all_users")]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="approved_app_reminders",
            field=models.BooleanField(
                default=False,
                help_text="Does this coordinator want approved app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="discussion_app_reminders",
            field=models.BooleanField(
                default=False,
                help_text="Does this coordinator want under discussion app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="pending_app_reminders",
            field=models.BooleanField(
                default=False,
                help_text="Does this coordinator want pending app reminder notices?",
            ),
        ),
    ]
