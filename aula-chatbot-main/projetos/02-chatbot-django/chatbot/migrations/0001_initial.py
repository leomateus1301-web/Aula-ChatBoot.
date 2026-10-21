# Generated for the educational chatbot project.
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='RespostaChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=250, unique=True)),
                ('resposta', models.TextField()),
            ],
            options={
                'verbose_name': 'Resposta do chatbot',
                'verbose_name_plural': 'Respostas do chatbot',
                'ordering': ['pergunta'],
            },
        ),
    ]
