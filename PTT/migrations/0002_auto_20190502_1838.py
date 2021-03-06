# Generated by Django 2.2.1 on 2019-05-02 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PTT', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='發文者'),
        ),
        migrations.AddField(
            model_name='post',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sorts', to='PTT.Sort', verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='PTT.Topic', verbose_name='版'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='留言者'),
        ),
        migrations.AddField(
            model_name='comment',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='PTT.Option', verbose_name='推/噓文'),
        ),
    ]
