from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to Load Google Gemini Model and provide query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows



prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Mydb and has the following columns - NAME,CLASS,
    SECTION \n\nFor Example 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM Mydb;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM Mydb
    where CLASS="Data Scientist";

    also the sql code should not have '''in beginning or end sql word in the output 
"""
]

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input:",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.header("The Response is")
    for row in data:
        print(row)
        st.header(row)

