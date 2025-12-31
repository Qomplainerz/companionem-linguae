import os
import django
from django.db import connection
from django.conf import settings

# Wichtig: Ersetze 'mein_projekt' durch den Namen deines Projektordners
# (das ist der Ordner, in dem die settings.py liegt).

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mein_projekt.settings')

# Django initialisieren

django.setup()

def test_mysql_connection():
    print(" Versuche Verbindung zur Datenbank herzustellen...")
    print(f"Ziel-Host: {settings,DATABASES['default']['HOST']}")

    try:
	# Cursor öffnen und eine einfache Abfrage senden
	with connection.cursor() as cursor:
	    cursor.execute("SELECT DATABASE(), VERSION()")
	    row = cursor.fetchone()

	    print("\n ERFOLG: Verbindung hergestellt!")
	    print(f"Verbundene Datenbank: {row[0]}")
	    print(f"MySQL Version: {row[1]}")

    except Exception as e:
	    print("\n FEHLER: Verbindung fehlgeschlagen.")
	    print(f"Fehlermeldung: {e}")

if __name__ == '__main__':
    test_mysql_connection()
