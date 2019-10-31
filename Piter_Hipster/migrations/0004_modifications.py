# Generated by Django 2.2.6 on 2019-10-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Piter_Hipster', '0003_photos_ismain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(max_length=100)),
                ('size', models.TextField(max_length=50)),
                ('id_goods', models.ForeignKey(on_delete='CASCADE', to='Piter_Hipster.Goods')),
            ],
        ),
    ]
