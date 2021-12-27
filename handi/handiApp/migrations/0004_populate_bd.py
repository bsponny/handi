from django.db import migrations, models

def populate_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Account = apps.get_model('handiApp', 'Account')

    admin = User.objects.create_user(username='admin', password='handiDandi')
    admin.save()

    account = Account(user=admin, userType=4, id=1)
    account.save()

class Migration(migrations.Migration):

    dependencies = [
        ('handiApp', '0003_auto_20211218_1216'),
    ]

    operations = [
        migrations.RunPython(populate_user),
    ]
    
