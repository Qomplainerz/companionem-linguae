import sqlite3

# Create database

conn = sqlite3.connect('001_DB_LAT_ENG_DICT.db')
cursor = conn.cursor()

# Create table headwords

cursor.execute('''
CREATE TABLE IF NOT EXISTS headwords (
    headword_id INTEGER PRIMARY KEY,
    lat TEXT NOT NULL UNIQUE,
    eng TEXT NOT NULL
)
''')

# Create table conjugations

cursor.execute('''
CREATE TABLE IF NOT EXISTS conjugations (
    conjugation_id INTEGER PRIMARY_KEY,
    ref_headword_id INTEGER,
    lat TEXT NOT NULL,
    eng TEXT NOT NULL,
    tense TEXT,
    person INTEGER,
    number TEXT,
    mood TEXT,
    FOREIGN KEY (ref_headword_id) REFERENCES headwords(headword_id)
)
''')

# Create table meanings

cursor.execute('''
CREATE TABLE IF NOT EXISTS meanings (
    meaning_id INTEGER PRIMARY KEY,
    ref_headword_id INTEGER,
    lat TEXT NOT NULL,
    eng TEXT NOT NULL,
    context TEXT,
    FOREIGN KEY (ref_headword_id) REFERENCES headwords(headword_id)
)
''')

# Create table usage_examples

cursor.execute('''
CREATE TABLE IF NOT EXISTS usage_examples (
    example_id INTEGER PRIMARY KEY,
    ref_conjugation_id INTEGER,
    ref_headword_id INTEGER,
    lat TEXT NOT NULL,
    eng TEXT NOT NULL,
    FOREIGN KEY (ref_conjugation_id) REFERENCES conjugations(conjugation_id),
    FOREIGN KEY (ref_headword_id) REFERENCES headwords(headword_id)
)
''')

# Insert headword

cursor.execute("INSERT OR IGNORE INTO headwords VALUES (1, 'discere', 'to learn')")

# Insert conjugations

conjugations = [
    (1, 1, 'discebam', 'I used to learn', 'imperfect', 1, 'sg', 'indicative'),
    (2, 1, 'discebas', 'you used to learn', 'imperfect', 2, 'sg', 'indicative'),
    (3, 1, 'discebat', 'it used to learn', 'imperfect', 3, 'sg', 'indicative'),
    (4, 1, 'discebamus', 'we used to learn', 'imperfect', 1, 'pl', 'indicative'),
    (5, 1, 'discebatis', 'you used to learn', 'imperfect', 2, 'pl', 'indicative'),
    (6, 1, 'discebant', 'they used to learn', 'imperfect', 3, 'pl', 'indicative'),
    (7, 1, 'didici', 'I learned', 'perfect', 1, 'sg', 'indicative'),
    (8, 1, 'didicisti', 'you learned', 'perfect', 2, 'sg', 'indicative'),
    (9, 1, 'didicit', 'it learned', 'perfect', 3, 'sg', 'indicative'),
    (10, 1, 'didicimus', 'we learned', 'perfect', 1, 'pl', 'indicative'),
    (11, 1, 'didicistis', 'you learned', 'perfect', 2, 'pl', 'indicative'),
    (12, 1, 'didicerunt', 'they learned', 'perfect', 3, 'pl', 'indicative'),
    (13, 1, 'discam', 'I will learn', 'future', 1, 'sg', 'indicative'),
    (14, 1, 'disces', 'you will learn', 'future', 2, 'sg', 'indicative'),
    (15, 1, 'discet', 'it will learn', 'future', 3, 'sg', 'indicative'),
    (16, 1, 'discemus', 'we will learn', 'future', 1, 'pl', 'indicative'),
    (17, 1, 'discetis', 'you will learn', 'future', 2, 'pl', 'indicative'),
    (18, 1, 'discent', 'they will learn', 'future', 3, 'pl', 'indicative'),
]

cursor.executemany('''
INSERT OR IGNORE INTO conjugations
(conjugation_id, ref_headword_id, lat, eng, tense, person, number, mood)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', conjugations)

# Insert meanings

cursor.execute("INSERT OR IGNORE INTO meanings VALUES (1, 1, 'discere', 'to learn', 'general')")
cursor.execute("INSERT OR IGNORE INTO meanings VALUES (2, 1, 'discere', 'to study', 'academic')")

# Insert usage examples

cursor.execute("INSERT OR IGNORE INTO usage_examples VALUES (1, 1, 1, 'Latine discebam in schola', 'I used to learn Latin in school')")
cursor.execute("INSERT OR IGNORE INTO usage_examples VALUES (2, 7, 1, 'Hodie Latine didici', 'Today I learned Latin')")

conn.commit()

# Test: Query

print("=== Test: Search 'discebam' ===")
cursor.execute("SELECT lat, eng, tense, person, number FROM conjugations WHERE lat = 'discebam'")
result = cursor.fetchone()
print("f{result[0]} = {result[1]} | Tense: {result[2]}, Person: {result[3]}, Number: {result[4]}\n")

# Test: All forms of discere

print("=== Test: All forms of 'discere' ===")
cursor.execute("""
SELECT lat, eng, tense, person, number
FROM conjugations
WHERE ref_headword_id = 1
ORDER BY conjugation_id
""")
for row in cursor.fetchall():
    print(f"{row[0]:15} = {row[1]:25} | {row[2]:10} {row[3]}/{row[4]}")
    
print("\n=== Test: Usage Examples ===")
cursor.execute("SELECT lat, eng FROM usage_examples")
for row in cursor.fetchall():
    print(f"{row[0]} -> {row[1]}")
    
conn.close()
print("\n Database created and tested successfully!")

