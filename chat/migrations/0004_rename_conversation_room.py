# Generated by Django 4.2 on 2023-04-11 15:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_conversation_message_conversation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conversation',
            new_name='Room',
        ),
    ]
