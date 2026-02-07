## PDF Plagiarism & Similarity Checker

##  Project Description

This project is an **Automated PDF Plagiarism & Similarity Checker** that detects semantic similarity between documents using **NLP and transformer-based embeddings**.

Instead of relying on exact word matching, the system converts PDF content into **sentence embeddings** and compares them using **cosine similarity**, making it robust to paraphrasing and rewording.

The results are stored in **MySQL**, enabling auditability and further analysis.


## Key Features

- Upload a new PDF for plagiarism checking
- Extract text automatically from PDFs
- Convert text into semantic embeddings
- Compare similarity with existing PDFs
- Flag high similarity (plagiarism risk)
- Store similarity results in MySQL
- Clean project structure with virtual environment


## How to run

1. Clone / Open the Project
cd pdf_similarity_checker

2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup MySQL Database

CREATE DATABASE pdf_similarity;

USE pdf_similarity;

CREATE TABLE similarity_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    new_pdf VARCHAR(255),
    compared_pdf VARCHAR(255),
    similarity_score FLOAT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

5. Configure Database Connection
Configure Database Connection inside db.py

6. Add PDF Files

Place one new PDF in:
data/input_pdfs/

Place existing reference PDFs in:
data/stored_pdfs/

7. Run the Application
python -m src.main

8. Results are also stored in MySQL:
SELECT * FROM similarity_results;