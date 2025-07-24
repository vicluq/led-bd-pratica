import os
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sql-postgres")

# Conexão com o Banco
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost", # DNS do banco na cloud
    port="5432"
)

cur = conn.cursor()

# Criando Tabelas
try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        login VARCHAR(10) UNIQUE NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        course VARCHAR(25) NOT NULL
    );
    """)
    conn.commit()
except Exception as err:
    logger.error(f"Error creating table: {err}")
    conn.rollback()
    os.system("exit 1")


# Inserindo Dados
try:
    cur.execute("INSERT INTO students (login, email, course) VALUES (%s, %s, %s);", ('vllst', 'vllst@cin.ufpe.br', 'Ciencia da Computação'))
    conn.commit()

    cur.execute("INSERT INTO students (login, email, course) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING;", ('legl', 'legl@cin.ufpe.br', 'Engenharia da Computação'))
    conn.commit()
except Exception as err:
    logger.error(f"Error inserting data: {err}")
    conn.rollback()
    os.system("exit 1")

# Realizando Queries
try:
    cur.execute("SELECT * FROM students WHERE login = 'vllst';")
    logger.info(cur.fetchone())

    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    logger.info(students)

    cur.execute("SELECT course FROM students;")
    courses = set([row[0] for row in cur.fetchall()])
    logger.info(courses)

    # DESAFIO: Quantidade de alunos por curso?
except Exception as err:
    logger.error(f"Error performing query: {err}")
    conn.rollback()
    os.system("exit 1")

conn.close()