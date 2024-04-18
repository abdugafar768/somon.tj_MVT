# Generated by Django 4.2 on 2024-03-25 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_basket_created_at_remove_basket_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.user'),
            preserve_default=False,
        ),
    ]
