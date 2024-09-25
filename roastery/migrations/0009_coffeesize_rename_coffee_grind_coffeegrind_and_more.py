# Generated by Django 4.2.11 on 2024-05-20 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roastery', '0008_alter_product_grind_id_alter_product_origin_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coffee_Grind',
            new_name='CoffeeGrind',
        ),
        migrations.RenameModel(
            old_name='Coffee_Origin',
            new_name='CoffeeOrigin',
        ),
         migrations.RenameModel(
            old_name='Coffee_Size',
            new_name='CoffeeSize',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='roastery.category', on_delete=django.db.models.deletion.CASCADE, related_name='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='grind_id',
            field=models.ForeignKey(to='roastery.coffeegrind', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin_id',
            field=models.ForeignKey(to='roastery.coffeeorigin', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_id',
            field=models.ForeignKey(to='roastery.coffeesize', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product'),
        ),
    ]
