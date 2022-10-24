# Generated by Django 3.2.16 on 2022-10-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True),
        ),
    ]