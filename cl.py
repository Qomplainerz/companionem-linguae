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
    pronoun TEXT,
    lat TEXT NOT NULL,
    eng TEXT NOT NULL,
    person INTEGER,
    number TEXT,
    voice TEXT,
    mood TEXT,
    tense TEXT,
    conjugation TEXT,
    pos TEXT,
    regularity TEXT,
    perf_stem_type TEXT,
    source TEXT,
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

# Insert headwords

headwords = [
    (1, 'discere', 'to learn')
]

cursor.executemany('''
INSERT OR IGNORE INTO headwords
(headword_id, lat, eng)
VALUES (?, ?, ?)
''', headwords)

# Insert conjugations

# --- KONJUGATIONEN EINFÜGEN ---
# Struktur: (ID, REF_ID, PRONOUN, LAT, ENG, PERSON, NUMERUS, VOICE, MOOD, TENSE, CONJUGATION, POS, REGULARITY, PERF_STEM_TYPE, SOURCE)

conjugations = [
    # --- DISCERE (to learn) - 3rd Conjugation ---
    # PRÄSENS (Present) - Aktiv (Active) - Indikativ (Indicative)
    
    (1, 1, 'ego', 'discō', 'I learn', 1, 'sg', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (2, 1, 'tū', 'discis', 'you learn', 2, 'sg', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (3, 1, 'is', 'discit', 'he/she/it learns', 3, 'sg', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (4, 1, 'nōs', 'díscimus', 'we learn', 1, 'pl', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (5, 1, 'vōs', 'díscitis', 'you learn', 2, 'pl', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (6, 1, 'iī', 'discunt', 'they learn', 3, 'pl', 'active', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PRÄSENS (Present) - Aktiv (Active) - Konjunktiv (Subjunctive)
    
    (7, 1, 'ego', 'discam', 'I may learn', 1, 'sg', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (8, 1, 'tū', 'discās', 'you may learn', 2, 'sg', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (9, 1, 'is', 'discat', 'he/she/it may learn', 3, 'sg', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (10, 1, 'nōs', 'discā́mus', 'we may learn', 1, 'pl', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (11, 1, 'vōs', 'discā́tis', 'you may learn', 2, 'pl', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (12, 1, 'iī', 'discant', 'they may learn', 3, 'pl', 'active', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PRÄSENS (Present) - Passiv (Passive) - Indikativ (Indicative)
    
    (13, 1, 'ego', 'discor', 'I am learned', 1, 'sg', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (14, 1, 'tū', 'dísceris', 'you are learned', 2, 'sg', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (15, 1, 'is', 'díscitur', 'he/she/it is learned', 3, 'sg', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (16, 1, 'nōs', 'díscimur', 'we are learned', 1, 'pl', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (17, 1, 'vōs', 'discíminī', 'you are learned', 2, 'pl', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (18, 1, 'iī', 'discúntur', 'they are learned', 3, 'pl', 'passive', 'indicative', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PRÄSENS (Present) - Passiv (Passive) - Konjunktiv (Subjunctive)
    
    (19, 1, 'ego', 'discar', 'I may be learned', 1, 'sg', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (20, 1, 'tū', 'discā́ris', 'you may be learned', 2, 'sg', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (21, 1, 'is', 'discā́tur', 'he/she/it may be learned', 3, 'sg', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (22, 1, 'nōs', 'discā́mur', 'we may be learned', 1, 'pl', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (23, 1, 'vōs', 'discā́minī', 'you may be learned', 2, 'pl', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (24, 1, 'iī', 'discā́ntur', 'they may be learned', 3, 'pl', 'passive', 'subjunctive', 'present', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # IMPERFEKT (Imperfect) - Aktiv (Active) - Indikativ (Indicative)
    
    (25, 1, 'ego', 'discḗbam', 'I used to learn', 1, 'sg', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (26, 1, 'tū', 'discḗbās', 'you used to learn', 2, 'sg', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (27, 1, 'is', 'discḗbat', 'he/she/it used to learn', 3, 'sg', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (28, 1, 'nōs', 'discēbā́mus', 'we used to learn', 1, 'pl', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (29, 1, 'vōs', 'discēbā́tis', 'you used to learn', 2, 'pl', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (30, 1, 'iī', 'discḗbant', 'they used to learn', 3, 'pl', 'active', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # IMPERFEKT (Imperfect) - Aktiv (Active) - Konjunktiv (Subjunctive)
    
    (31, 1, 'ego', 'discerem', 'I might learn / I would learn', 1, 'sg', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (32, 1, 'tū', 'discerēs', 'you might learn', 2, 'sg', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (33, 1, 'is', 'disceret', 'he/she/it might learn', 3, 'sg', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (34, 1, 'nōs', 'discerḗmus', 'we might learn', 1, 'pl', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (35, 1, 'vōs', 'discerḗtis', 'you might learn', 2, 'pl', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (36, 1, 'iī', 'discerent', 'they might learn', 3, 'pl', 'active', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # IMPERFEKT (Imperfect) - Passiv (Passive) - Indikativ (Indicative)
    
    (37, 1, 'ego', 'discḗbar', 'I was being learned', 1, 'sg', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (38, 1, 'tū', 'discēbā́ris', 'you were being learned', 2, 'sg', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (39, 1, 'is', 'discēbā́tur', 'he/she/it was being learned', 3, 'sg', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (40, 1, 'nōs', 'discēbā́mur', 'we were being learned', 1, 'pl', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (41, 1, 'vōs', 'discēbā́minī', 'you were being learned', 2, 'pl', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (42, 1, 'iī', 'discēbántur', 'they were being learned', 3, 'pl', 'passive', 'indicative', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # IMPERFEKT (Imperfect) - Passiv (Passive) - Konjunktiv (Subjunctive)
    
    (43, 1, 'ego', 'discerer', 'I might be learned', 1, 'sg', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (44, 1, 'tū', 'discerḗris', 'you might be learned', 2, 'sg', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (45, 1, 'is', 'discerḗtur', 'he/she/it might be learned', 3, 'sg', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (46, 1, 'nōs', 'discerḗmur', 'we might be learned', 1, 'pl', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (47, 1, 'vōs', 'discerḗminī', 'you might be learned', 2, 'pl', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (48, 1, 'iī', 'discerḗntur', 'they might be learned', 3, 'pl', 'passive', 'subjunctive', 'imperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # FUTUR I (I Future) - Aktiv (Active) - Indikativ (Indicative)
    
    (49, 1, 'ego', 'discam', 'I will learn', 1, 'sg', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (50, 1, 'tū', 'discēs', 'you will learn', 2, 'sg', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (51, 1, 'is', 'discet', 'he/she/it will learn', 3, 'sg', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (52, 1, 'nōs', 'discḗmus', 'we will learn', 1, 'pl', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (53, 1, 'vōs', 'discḗtis', 'you will learn', 2, 'pl', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (54, 1, 'iī', 'discent', 'they will learn', 3, 'pl', 'active', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # FUTUR I (I Future) - Passiv (Passive) - Indikativ (Indicative)
    
    (55, 1, 'ego', 'discar', 'I will be learned', 1, 'sg', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (56, 1, 'tū', 'discḗris', 'you will be learned', 2, 'sg', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (57, 1, 'is', 'discḗtur', 'he/she/it will be learned', 3, 'sg', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (58, 1, 'nōs', 'discḗmur', 'we will be learned', 1, 'pl', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (59, 1, 'vōs', 'discḗminī', 'you will be learned', 2, 'pl', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (60, 1, 'iī', 'discéntur', 'they will be learned', 3, 'pl', 'passive', 'indicative', 'future', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    
    # PERFEKT (Perfect) - Aktiv (Active) - Indikativ (Indicative) - Einfach
    
    (61, 1, 'ego', 'didicī', 'I learned / I have learned', 1, 'sg', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (62, 1, 'tū', 'didicístī', 'you learned / you have learned', 2, 'sg', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (63, 1, 'is', 'didicit', 'he/she/it learned / has learned', 3, 'sg', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (64, 1, 'nōs', 'didicimus', 'we learned / we have learned', 1, 'pl', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (65, 1, 'vōs', 'didicístis', 'you learned / you have learned', 2, 'pl', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (66, 1, 'iī', 'didicḗrunt', 'they learned / they have learned', 3, 'pl', 'active', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    
    # PERFEKT (Perfect) - Aktiv (Active) - Konjunktiv (Subjunctive)
    
    (67, 1, 'ego', 'didícerim', 'I may have learned', 1, 'sg', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (68, 1, 'tū', 'didíceris', 'you may have learned', 2, 'sg', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (69, 1, 'is', 'didícerit', 'he/she/it may have learned', 3, 'sg', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (70, 1, 'nōs', 'didicérimus', 'we may have learned', 1, 'pl', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (71, 1, 'vōs', 'didicéritis', 'you may have learned', 2, 'pl', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (72, 1, 'iī', 'didícerint', 'they may have learned', 3, 'pl', 'active', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PERFEKT (Perfect) - Passiv (Passive) - Indikativ (Composite Tense)
    
    (73, 1, 'ego', 'discus sum', 'I was learned / I have been learned', 1, 'sg', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (74, 1, 'tū', 'discus es', 'you were learned / you have been learned', 2, 'sg', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (75, 1, 'is', 'discus est', 'he/she/it was learned / has been learned', 3, 'sg', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (76, 1, 'nōs', 'discī sumus', 'we were learned / we have been learned', 1, 'pl', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (77, 1, 'vōs', 'discī estis', 'you were learned / you have been learned', 2, 'pl', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (78, 1, 'iī', 'discī sunt', 'they were learned / they have been learned', 3, 'pl', 'passive', 'indicative', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PERFEKT (Perfect) - Passiv (Passive) - Konjunktiv (Composite Tense)
    
    (79, 1, 'ego', 'discus sim', 'I may have been learned', 1, 'sg', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (80, 1, 'tū', 'discus sīs', 'you may have been learned', 2, 'sg', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (81, 1, 'is', 'discus sit', 'he/she/it may have been learned', 3, 'sg', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (82, 1, 'nōs', 'discī sīmus', 'we may have been learned', 1, 'pl', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (83, 1, 'vōs', 'discī sītis', 'you may have been learned', 2, 'pl', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (84, 1, 'iī', 'discī sint', 'they may have been learned', 3, 'pl', 'passive', 'subjunctive', 'perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    
    # PLUSQUAMPERFEKT (Pluperfect) - Aktiv (Active) - Indikativ (Indicative)
    
    (85, 1, 'ego', 'didíceram', 'I had learned', 1, 'sg', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (86, 1, 'tū', 'didícerās', 'you had learned', 2, 'sg', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (87, 1, 'is', 'didícerat', 'he/she/it had learned', 3, 'sg', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (88, 1, 'nōs', 'didicerā́mus', 'we had learned', 1, 'pl', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (89, 1, 'vōs', 'didicerā́tis', 'you had learned', 2, 'pl', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (90, 1, 'iī', 'didícerant', 'they had learned', 3, 'pl', 'active', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    
    # PLUSQUAMPERFEKT (Pluperfect) - Aktiv (Active) - Konjunktiv (Subjunctive)
    
    (91, 1, 'ego', 'didicíssem', 'I might have learned / I would have learned', 1, 'sg', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (92, 1, 'tū', 'didicíssēs', 'you might have learned', 2, 'sg', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (93, 1, 'is', 'didicísset', 'he/she/it might have learned', 3, 'sg', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (94, 1, 'nōs', 'didicissḗmus', 'we might have learned', 1, 'pl', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (95, 1, 'vōs', 'didicissḗtis', 'you might have learned', 2, 'pl', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (96, 1, 'iī', 'didicíssent', 'they might have learned', 3, 'pl', 'active', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PLUSQUAMPERFEKT (Pluperfect) - Passiv (Passive) - Indikativ (Composite Tense)
    
    (97, 1, 'ego', 'discus eram', 'I had been learned', 1, 'sg', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (98, 1, 'tū', 'discus erās', 'you had been learned', 2, 'sg', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (99, 1, 'is', 'discus erat', 'he/she/it had been learned', 3, 'sg', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (100, 1, 'nōs', 'discī erāmus', 'we had been learned', 1, 'pl', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (101, 1, 'vōs', 'discī erātis', 'you had been learned', 2, 'pl', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (102, 1, 'iī', 'discī erant', 'they had been learned', 3, 'pl', 'passive', 'indicative', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # PLUSQUAMPERFEKT (Pluperfect) - Passiv (Passive) - Konjunktiv (Composite Tense)
    
    (103, 1, 'ego', 'discus essem', 'I might have been learned', 1, 'sg', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (104, 1, 'tū', 'discus essēs', 'you might have been learned', 2, 'sg', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (105, 1, 'is', 'discus esset', 'he/she/it might have been learned', 3, 'sg', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (106, 1, 'nōs', 'discī essēmus', 'we might have been learned', 1, 'pl', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (107, 1, 'vōs', 'discī essētis', 'you might have been learned', 2, 'pl', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (108, 1, 'iī', 'discī essent', 'they might have been learned', 3, 'pl', 'passive', 'subjunctive', 'pluperfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # FUTUR II (II Future) - Aktiv (Active) - Indikativ (Indicative)
    
    (109, 1, 'ego', 'didícerō', 'I will have learned', 1, 'sg', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (110, 1, 'tū', 'didíceris', 'you will have learned', 2, 'sg', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (111, 1, 'is', 'didícerit', 'he/she/it will have learned', 3, 'sg', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (112, 1, 'nōs', 'didicérimus', 'we will have learned', 1, 'pl', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (113, 1, 'vōs', 'didicéritis', 'you will have learned', 2, 'pl', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (114, 1, 'iī', 'didícerint', 'they will have learned', 3, 'pl', 'active', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),

    # FUTUR II (II Future) - Passiv (Passive) - Indikativ (Composite Tense)
    
    (115, 1, 'ego', 'discus erō', 'I will have been learned', 1, 'sg', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (116, 1, 'tū', 'discus eris', 'you will have been learned', 2, 'sg', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (117, 1, 'is', 'discus erit', 'he/she/it will have been learned', 3, 'sg', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (118, 1, 'nōs', 'discī erimus', 'we will have been learned', 1, 'pl', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (119, 1, 'vōs', 'discī eritis', 'you will have been learned', 2, 'pl', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (120, 1, 'iī', 'discī erunt', 'they will have been learned', 3, 'pl', 'passive', 'indicative', 'future perfect', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    
    # IMPERATIV (Imperative) - Aktiv (Active) - Indikativ/Subjunktiv
    
    (121, 1, 'tū', 'disce', 'Learn!', 2, 'sg', 'active', 'imperative', 'imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (122, 1, 'vōs', 'díscite', 'Learn! (pl.)', 2, 'pl', 'active', 'imperative', 'imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (123, 1, 'tū', 'díscitō', 'You shall learn!', 2, 'sg', 'active', 'imperative', 'future imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (124, 1, 'is', 'díscitō', 'He/she/it shall learn!', 3, 'sg', 'active', 'imperative', 'future imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (125, 1, 'vōs', 'discitṓte', 'You shall learn! (pl.)', 2, 'pl', 'active', 'imperative', 'future imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
    (126, 1, 'iī', 'discúntō', 'They shall learn!', 3, 'pl', 'active', 'imperative', 'future imperative', 'third', 'verb', 'irregular', 'didici', 'https://www.verbix.com/webverbix/go.php?T1=d%C4%ABscere&D1=9&H1=109'),
]

cursor.executemany('''
INSERT OR IGNORE INTO conjugations
(conjugation_id, ref_headword_id, pronoun, lat, eng, person, number, voice, mood, tense, conjugation, pos, regularity, perf_stem_type, source)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', conjugations)

# Insert meanings

meanings = [
    (1, 1, 'discere', 'to learn', 'general'),
    (2, 1, 'discere', 'to study', 'academic')
]

cursor.executemany('''
INSERT OR IGNORE INTO meanings
(meaning_id, ref_headword_id, lat, eng, context)
VALUES (?, ?, ?, ?, ?)
''', meanings)

# Insert usage examples

usage_examples = [
    (1, 1, 1, 'Latine discebam in schola', 'I used to learn Latin in school'),
    (2, 7, 1, 'Hodie Latine didici', 'Today I learned Latin')
]

cursor.executemany('''
INSERT OR IGNORE INTO usage_examples
(example_id, ref_conjugation_id, ref_headword_id, lat, eng)
VALUES (?, ?, ?, ?, ?)
''', usage_examples)

conn.commit()

# Close the database

conn.close()
print("\n Database created and tested successfully!")

