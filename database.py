import sqlite3
from datetime import datetime

# 📦 SQLite Connection Setup
conn = sqlite3.connect("herguide.db", check_same_thread=False)
cursor = conn.cursor()

# ─── Create Tables ──────────────────────────────────────────────
def create_tables():
    # Q&A Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Yojana Recommendations Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS yojana_recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            salary REAL,
            state TEXT,
            suggestion TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # SkillHer Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skillher_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            business TEXT,
            contact TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Scam Reports
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suraksha_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            flagged INTEGER,
            reason TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Feedback Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            message TEXT,
            feedback TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()

# ─── Insert Functions ────────────────────────────────────
def insert_question(question, answer):
    print("Inserting Question:", question, answer)
    cursor.execute("INSERT INTO questions_log (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()

def insert_yojana(name, age, salary, state, suggestion):
    cursor.execute('''
        INSERT INTO yojana_recommendations (name, age, salary, state, suggestion)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, salary, state, suggestion))
    conn.commit()

def insert_profile(name, location, business, contact):
    cursor.execute('''
        INSERT INTO skillher_profiles (name, location, business, contact)
        VALUES (?, ?, ?, ?)
    ''', (name, location, business, contact))
    conn.commit()

def insert_scam(message, flagged, reason):
    cursor.execute('''
        INSERT INTO suraksha_reports (message, flagged, reason)
        VALUES (?, ?, ?)
    ''', (message, int(flagged), reason))
    conn.commit()

def insert_feedback(source, message, feedback):
    cursor.execute('''
        INSERT INTO feedback_log (source, message, feedback)
        VALUES (?, ?, ?)
    ''', (source, message, feedback))
    conn.commit()

# ─── Fetch Functions ─────────────────────────────────────
def fetch_profiles():
    cursor.execute("SELECT name, location, business, contact FROM skillher_profiles ORDER BY timestamp DESC")
    return cursor.fetchall()

def fetch_questions():
    cursor.execute("SELECT question, answer, timestamp FROM questions_log ORDER BY timestamp DESC")
    return cursor.fetchall()

def fetch_yojanas():
    cursor.execute("SELECT name, state, suggestion, timestamp FROM yojana_recommendations ORDER BY timestamp DESC")
    return cursor.fetchall()

def fetch_scams():
    cursor.execute("SELECT message, flagged, reason, timestamp FROM suraksha_reports ORDER BY timestamp DESC")
    return cursor.fetchall()

# ─── Main Function for Test Data ─────────────────────────
if __name__ == "__main__":
    create_tables()
    insert_question("मुझे लोन कैसे मिलेगा?", "आप मुद्रा योजना के लिए अप्लाई कर सकती हैं।")
    insert_yojana("राधा", 35, 200000.0, "उत्तर प्रदेश", "जनधन योजना")
    insert_profile("सीमा", "दिल्ली", "सिलाई का काम", "9876543210")
    insert_scam("जल्दी भुगतान करें वरना अकाउंट बंद हो जाएगा", True, "संभावित स्कैम")

    print("Inserted sample data ✅")
