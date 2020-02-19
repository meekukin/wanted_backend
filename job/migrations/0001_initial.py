# Generated by Django 3.0.3 on 2020-02-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.URLField(max_length=50)),
                ('details', models.TextField(max_length=2000)),
                ('salary', models.IntegerField()),
                ('staff', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=2000)),
                ('details', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company')),
            ],
            options={
                'db_table': 'job_postings',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='JobUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_posting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobPosting')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'job_users',
            },
        ),
        migrations.AddField(
            model_name='jobposting',
            name='like',
            field=models.ManyToManyField(through='job.JobUser', to='user.User'),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.SubCategory'),
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.Company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'company_users',
            },
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Tag')),
            ],
            options={
                'db_table': 'company_tags',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='follow',
            field=models.ManyToManyField(through='job.CompanyUser', to='user.User'),
        ),
        migrations.AddField(
            model_name='company',
            name='tag',
            field=models.ManyToManyField(through='job.CompanyTag', to='job.Tag'),
        ),
    ]