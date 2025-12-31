from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json

# @csrf_exempt erlaubt uns erstmal den Zugriff ohne Sicherheits-Token (für den Anfang einfacher)
@csrf_exempt 
def chat_api(request):
    if request.method == 'POST':
        # 1. Nachricht vom JavaScript empfangen
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # 2. Verbindung zur Datenbank testen (Logik aus test_connection.py)
        db_status = "Nicht verbunden"
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE()")
                row = cursor.fetchone()
                db_status = f"Verbunden mit {row[0]}"
        except Exception as e:
            db_status = f"Fehler: {str(e)}"

        # 3. Antwort generieren
        bot_response = f"Ich habe '{user_message}' erhalten. Status: {db_status}"

        return JsonResponse({'reply': bot_response})
    
    return JsonResponse({'error': 'Nur POST erlaubt'}, status=400)
