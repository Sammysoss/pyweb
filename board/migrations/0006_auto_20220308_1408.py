# Generated by Django 3.1.3 on 2022-03-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_answer_modify_date_question_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]