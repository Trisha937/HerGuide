
import mysql.connector

# 🔐 MySQL connection config
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Herguide@123",
    database="herguide"
)
cursor = conn.cursor()

# ─── Create Tables ──────────────────────────────────────────────
def create_tables():
    # Q&A Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions_log (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question TEXT,
            answer TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Yojana Recommendations Table (From Form: नाम, उम्र, आय, राज्य)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS yojana_recommendations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            salary FLOAT,
            state VARCHAR(100),
            suggestion TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # SkillHer Table (From Form: नाम, स्थान, व्यवसाय, संपर्क)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skillher_profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            location VARCHAR(100),
            business VARCHAR(200),
            contact VARCHAR(100),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Scam Reports (From input: message, flagged, reason)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suraksha_reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT,
            flagged BOOLEAN,
            reason TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()

# ─── Insert Functions ────────────────────────────────────
def insert_question(question, answer):
    print("Inserting Question:", question, answer)
    cursor.execute("INSERT INTO questions_log (question, answer) VALUES (%s, %s)", (question, answer))
    conn.commit()

def insert_yojana(name, age, salary, state, suggestion):
    cursor.execute('''
        INSERT INTO yojana_recommendations (name, age, salary, state, suggestion)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, age, salary, state, suggestion))
    conn.commit()

def insert_profile(name, location, business, contact):
    cursor.execute('''
        INSERT INTO skillher_profiles (name, location, business, contact)
        VALUES (%s, %s, %s, %s)
    ''', (name, location, business, contact))
    conn.commit()

def insert_scam(message, flagged, reason):
    cursor.execute('''
        INSERT INTO suraksha_reports (message, flagged, reason)
        VALUES (%s, %s, %s)
    ''', (message, int(flagged), reason))
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


if __name__ == "__main__":
    create_tables()
    insert_question("मुझे लोन कैसे मिलेगा?", "आप मुद्रा योजना के लिए अप्लाई कर सकती हैं।")
    insert_yojana("राधा", 35, 200000.0, "उत्तर प्रदेश", "जनधन योजना")
    insert_profile("सीमा", "दिल्ली", "सिलाई का काम", "9876543210")
    insert_scam("जल्दी भुगतान करें वरना अकाउंट बंद हो जाएगा", True, "संभावित स्कैम")

    print("Inserted sample data ✅")
