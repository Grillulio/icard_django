# Generated by Django 4.2.5 on 2023-10-06 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paymentType', models.CharField(choices=[('CARD', 'card'), ('CASH', 'cash')], max_length=255)),
                ('statusPayment', models.CharField(choices=[('PENDING', 'pending'), ('PAID', 'paid')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
