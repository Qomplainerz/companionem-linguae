import mysql.connector
from mysql.connector import Error

def create_database_and_tables():
    connection = None  # Variable initialisieren
    try:
        # Connect to MySQL-Server
        
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'your username', # Replace this with your username
            password = 'your password' # Replace this with your password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS 001_DB_CL")
            print("Database 001_DB_CL was created or exists already")
            
            # Switch to database
            
            cursor.execute("USE 001_DB_CL")
            
            # Create table 001_TBL_TENSES
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 001_TBL_TENSES (
                TENSE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                TENSE VARCHAR(255)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 001_TBL_TENSES was created successfully")
            
            # Create table 002_TBL_MOODS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 002_TBL_MOODS (
                MOOD_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                MOOD VARCHAR(255)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 002_TBL_MOODS was created successfully")
            
            # Create table 003_TBL_PERSONS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 003_TBL_PERSONS (
                PERSON_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                PERSON INTEGER
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 003_TBL_PERSONS was created successfully")
            
            # CREATE TABLE 004_TBL_NUMERUS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 004_TBL_NUMERUS (
                NUMERUS_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                NUMERUS VARCHAR(2)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 004_TBL_NUMERUS was created successfully")
            
            # Create table 005_TBL_CONJUGATION_PATTERNS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 005_TBL_CONJUGATION_PATTERNS (
                CONJUGATION_PATTERN_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                CONJUGATION_PATTERN VARCHAR(10)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 005_TBL_CONJUGATION_PATTERNS was created successfully")
            
            # CREATE table 006_TBL_POS_TAGS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 006_TBL_POS_TAGS (
                POS_TAG_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                POS_TAG VARCHAR(20)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 006_TBL_POS_TAGS was created successfully")
            
            # Create table 007_TBL_REGULARITY
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 007_TBL_REGULARITY (
                REGULARITY_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                REGULARITY VARCHAR(15)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 007_TBL_REGULARITY was created successfully")
            
            # CREATE table 008_TBL_LANGS
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 008_TBL_LANGS (
                LANG_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                LANG VARCHAR(125)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 008_TBL_LANGS was created successfully")

            # Create table 009_TBL_LEXEMES
            # This table stores the root forms of words and links them with lookup-tables
            # The JSON field 'GRAMMAR_METADATA_JSON' saves variable properties (i. e. perfec stem, declination type)
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 009_TBL_LEXEMES(
                LEXEME_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                REF_LANG_ID INTEGER NOT NULL,
                REF_POS_TAG_ID INTEGER NOT NULL,
                LAT_LEMMA VARCHAR(255) NOT NULL,
                
                # JSON field for all grammatical metadata
                # i. e. genus (for nouns), perfect stem (for verbs), comparative forms (for adjectives)
                GRAMMAR_METADATA_JSON JSON,
                
                FOREIGN KEY (REF_LANG_ID) REFERENCES 008_TBL_LANGS(LANG_ID),
                FOREIGN KEY (REF_POS_TAG_ID) REFERENCES 006_TBL_POS_TAGS(POS_TAG_ID)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 009_TBL_LEXEMES was created successfully.")
            
            # Creates another main table (conjugations/declinations)
            # Stores all flected forms of a word
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS 010_TBL_FORMS(
                FORM_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                REF_LEXEME_ID INTEGER NOT NULL,
                REF_TENSE_ID INTEGER,
                REF_MOOD_ID INTEGER,
                
                # Using JSON hybrid here as well
                # person, numerus, gender, case, polarity etc.
                FORM_METADATA_JSON JSON,
                
                LAT_FORM VARCHAR(255) NOT NULL,
                ENG_TRANSLATION VARCHAR(255) NOT NULL,
                
                FOREIGN KEY (REF_LEXEME_ID) REFERENCES 009_TBL_LEXEMES(LEXEME_ID),
                FOREIGN KEY (REF_TENSE_ID) REFERENCES 001_TBL_TENSES(TENSE_ID),
                FOREIGN KEY (REF_MOOD_ID) REFERENCES 002_TBL_MOODS(MOOD_ID)
            )
            """
            cursor.execute(create_table_query)
            
            print("Table 010_TBL_FORMS was created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
            
# Execute
create_database_and_tables()
