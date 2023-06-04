# Generated by Django 4.2.1 on 2023-06-03 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('seller_type', models.PositiveSmallIntegerField(choices=[(1, 'Завод'), (2, 'Розничная сеть'), (3, 'Индивидуальный предприниматель')])),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('country', models.CharField(verbose_name='Страна')),
                ('city', models.CharField(verbose_name='Город')),
                ('street', models.CharField(verbose_name='Улица')),
                ('house_number', models.CharField(verbose_name='Номер дома')),
                ('debt', models.FloatField(default=0.0, verbose_name='Задолженность перед поставщиком')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')),
                ('products', models.ManyToManyField(blank=True, null=True, to='products.product', verbose_name='Продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sellers.seller', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
            },
        ),
    ]
