# Generated by Django 3.1 on 2021-12-10 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPart', models.CharField(max_length=200)),
                ('logoPart', models.ImageField(upload_to='partenaire')),
            ],
        ),
        migrations.CreateModel(
            name='PubAcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub1', models.FileField(upload_to='puba')),
                ('nonEntrep', models.CharField(blank=True, max_length=50, null=True)),
                ('messag1', models.CharField(blank=True, max_length=700, null=True)),
                ('messag2', models.CharField(blank=True, max_length=700, null=True)),
                ('lien', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PubChangp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub5', models.FileField(upload_to='pubchan')),
                ('lien', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PubConnect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub3', models.FileField(upload_to='pubcon')),
                ('lien', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PubCrecomp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub4', models.FileField(upload_to='pubcc')),
                ('lien', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PubDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub2', models.FileField(upload_to='pubd')),
                ('lien', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prix', models.IntegerField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('numero', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=50)),
                ('taille', models.FloatField()),
                ('tein', models.CharField(blank=True, max_length=100, null=True)),
                ('forme', models.CharField(blank=True, max_length=100, null=True)),
                ('quartier', models.CharField(blank=True, max_length=100, null=True)),
                ('image1', models.ImageField(upload_to='img/maison')),
                ('image2', models.ImageField(upload_to='img/maison')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('description', models.TextField(blank=True, null=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.age')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commune')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Plusdemande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prix', models.IntegerField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('numero', models.CharField(max_length=20)),
                ('taille', models.FloatField()),
                ('tein', models.CharField(blank=True, max_length=100, null=True)),
                ('forme', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quartier', models.CharField(blank=True, max_length=100, null=True)),
                ('image1', models.ImageField(upload_to='img/maison')),
                ('image2', models.ImageField(upload_to='img/maison')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='img/maison')),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.age')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commune')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ville')),
            ],
        ),
    ]
