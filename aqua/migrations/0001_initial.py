# Generated by Django 4.0.3 on 2022-08-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('request_from', models.CharField(choices=[(1, 'From Contact Page'), (2, 'From About Page'), (3, 'From Service Page')], default=0, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('describe_1', models.TextField(blank=True, null=True)),
                ('describe_2', models.TextField(blank=True, null=True)),
                ('describe_3', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='upload/product_image')),
                ('price', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[(1, 'Active'), (2, 'Deactivate'), (3, 'Delete')], default=1, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Qutation_for_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aqua.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
