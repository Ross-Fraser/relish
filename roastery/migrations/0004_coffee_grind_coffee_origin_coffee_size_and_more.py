# Generated by Django 4.2.11 on 2024-05-16 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roastery', '0003_coffeeproduct_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_Grind',
            fields=[
                ('grind_id', models.AutoField(primary_key=True, serialize=False)),
                ('grind', models.IntegerField(choices=[(0, 'Whole Bean'), (1, 'Coarse'), (2, 'Medium'), (3, 'Fine'), (4, 'Extra Fine')])),
            ],
        ),
        migrations.CreateModel(
            name='Coffee_Origin',
            fields=[
                ('origin_id', models.AutoField(primary_key=True, serialize=False)),
                ('continent', models.IntegerField(choices=[(0, 'Africa'), (1, 'Asia'), (2, 'Americas')])),
                ('country', models.IntegerField(choices=[(0, 'Ethiopia'), (1, 'Kenya'), (2, 'Uganda'), (3, 'India'), (4, 'Vietnam'), (5, 'Brazil'), (6, 'Colombia'), (7, 'Guatemala'), (8, 'Peru')])),
                ('region', models.IntegerField(choices=[(0, 'Sidamo'), (1, 'Blue Mountain'), (2, 'Agua Santa'), (3, 'Excelso Popayan'), (4, 'Huehuetenango'), (5, 'Copaceyba'), (6, 'Malabar')])),
            ],
        ),
        migrations.CreateModel(
            name='Coffee_Size',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coffee_Variant',
            fields=[
                ('variant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Coffee_Variant', to='roastery.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='coffee_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='roastery.category'),
        ),
        migrations.DeleteModel(
            name='CoffeeProduct',
        ),
        migrations.AddField(
            model_name='product',
            name='coffee_variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='roastery.coffee_variant'),
        ),
        migrations.AddField(
            model_name='product',
            name='grind_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Coffee_Variant', to='roastery.coffee_grind'),
        ),
        migrations.AddField(
            model_name='product',
            name='origin_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Coffee_Variant', to='roastery.coffee_origin'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Coffee_Variant', to='roastery.coffee_size'),
        ),
    ]