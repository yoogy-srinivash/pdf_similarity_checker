import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="pdf_similarity"
    )

def save_result(new_pdf, compared_pdf, score, status):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO similarity_results
    (new_pdf, compared_pdf, similarity_score, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (new_pdf, compared_pdf, score, status))
    conn.commit()

    cursor.close()
    conn.close()
