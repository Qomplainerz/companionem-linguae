import mysql.connector
from mysql.connector import Error

def insert_data():
    connection = None
    try:
        # Connect to MySQL-Server
        
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'username', # Replace this with your username
            password = 'password', # Replace this with your password
            database = '001_DB_CL'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Insert data into 001_TBL_TENSES
            
            tenses_data = [
                ('Present',),
                ('Imperfect',),
                ('Future',),
                ('Perfect',),
                ('Pluperfect',),
                ('Future Perfect',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 001_TBL_TENSES (TENSE) VALUES (%s)",
                tenses_data
            )
            
            print(f"{cursor.rowcount} rows inserted into 001_TBL_TENSES")
            
            # Insert data into 002_TBL_MOODS
            
            moods_data = [
                ('Indicative',),
                ('Subjunctive',),
                ('Imperative',),
                ('Infinitive',),
                ('Participle',),
                ('Gerund',),
                ('Supine',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 002_TBL_MOODS (MOOD) VALUES (%s)",
                moods_data
            )
            
            print(f"{cursor.rowcount} rows inserted into 002_TBL_MOODS")
            
            # Insert data into 003_TBL_PERSONS
            
            persons_data = [
                (1,),
                (2,),
                (3,)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 003_TBL_PERSONS (PERSON) VALUES (%s)",
                persons_data
            )
            
            print(f"{cursor.rowcount} rows inserted into 003_TBL_PERSONS")
            
            # Insert data into 004_TBL_NUMERUS
            
            numerus_data = [
                ('SG',), # Singular
                ('PL',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 004_TBL_NUMERUS (NUMERUS) VALUES (%s)",
                numerus_data
            )
            print(f"{cursor.rowcount} rows inserted into 004_TBL_NUMERUS")
            
            # Insert data into 005_TBL_CONJUGATION_PATTERNS
            
            conjugation_patterns_data = [
                ('1st',), # -are verbs (amare)
                ('2nd',), # -ēre verbs (monēre)
                ('3rd',), # -ere verbs (legere)
                ('3rd-io',), # -ere verbs with -io (capere)
                ('4th',), # -ire verbs (audire)
                ('irregular',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 005_TBL_CONJUGATION_PATTERNS (CONJUGATION_PATTERN) VALUES (%s)",
                conjugation_patterns_data
            )
            print(f"{cursor.rowcount} rows inserted into 005_TBL_CONJUGATION_PATTERNS")
            
            # Insert data into 006_TBL_POS_TAGS
            
            pos_tags_data = [
                ('VERB',),
                ('NOUN',),
                ('ADJ',),
                ('ADV',),
                ('PRON',),
                ('PREP',),
                ('CONJ',),
                ('INTERJ',),
                ('PART',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 006_TBL_POS_TAGS (POS_TAG) VALUES (%s)",
                pos_tags_data
            )
            print(f"{cursor.rowcount} rows inserted into 006_TBL_POS_TAGS")
            
            # Insert data into 007_TBL_REGULARITY
            
            regularity_data = [
                ('regular',),
                ('irregular',),
                ('semi-irregular',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 007_TBL_REGULARITY (REGULARITY) VALUES (%s)",
                regularity_data
            )
            print(f"{cursor.rowcount} rows inserted into 007_TBL_REGULARITY")
            
            # Insert data into 008_TBL_LANGS
            
            langs_data = [
                ('Latin',),
                ('English',),
                ('Marubo',),
                ('Ancient Greek',),
                ('German',)
            ]
            
            cursor.executemany(
                "INSERT IGNORE INTO 008_TBL_LANGS (LANG) VALUES (%s)",
                langs_data
            )
            print(f"{cursor.rowcount} rows inserted into 008_TBL_LANGS")
            
            # Commit all changes
            
            connection.commit()
            print("\nAll data inserted successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()
            
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
            
# Execute

insert_data()
