import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# -------------------------------------------------
# Environment & Config
# -------------------------------------------------

load_dotenv()

DB_CONFIG =
{
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": "utf8mb4",
    "collation": "utf8mb4_general_ci"
}

# -------------------------------------------------
# Flask App
# -------------------------------------------------

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# -------------------------------------------------
# Helper: DB Connection
# -------------------------------------------------

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.route("/api/verses", methods=["GET"])
def get_verses():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify(
        {
            "error": "Query parameter 'q' is required"
        }), 400

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        if query.isdigit():
            sql = """
                SELECT
                    source,
                    doc,
                    chapter,
                    verse,
                    content
                FROM `003_tbl_phrases`
                WHERE verse = %s
                ORDER BY verse
            """
            cursor.execute(sql, (query,))
        else:
            sql = """
                SELECT
                    source,
                    doc,
                    chapter,
                    verse,
                    content
                FROM `003_tbl_phrases`
                WHERE content LIKE %s
                ORDER BY chapter, verse
                LIMIT 25
            """
            cursor.execute(sql, (f"%{query}%",))

        rows = cursor.fetchall()

        return jsonify(
        {
            "count": len(rows),
            "results": rows
        })

    except Error as err:
        app.logger.error(f"Database error: {err}")
        return jsonify(
        {
            "error": "Internal server error"
        }), 500

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals() and conn.is_connected():
            conn.close()

# -------------------------------------------------
# Health Check (Deployment wichtig)
# -------------------------------------------------

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# -------------------------------------------------
# Entry Point (NICHT für Production-WSGI!)
# -------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
