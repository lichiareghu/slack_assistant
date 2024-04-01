import logging
from application_factory import db
from modules.chat_factory import Completions
#from modules.chat_factory import ChatWithAssistant


def query_database(db_question):
    context = [
        {"role": "system", "content": '''You are an assistant who writes SQL queries for the table described as 
                                      ####CREATE TABLE sakila.movies_and_tv (
                                                                            show_id int PRIMARY KEY,
                                                                            cast text,
                                                                            country text,
                                                                            date_added text,
                                                                            description text,
                                                                            director text,
                                                                            duration text,
                                                                            listed_in text,
                                                                            rating text,
                                                                            release_year int,
                                                                            title text,
                                                                            type text)####'''},
        {"role": "user",
         "content": f"Write an SQL query to answer the question '{db_question}'"}
    ]
    # Initialise ChatResponse object
    comp = Completions()

    # Generate chat response
    res = comp.generate_response(context)
    logging.info(f"Response::{res}")

    # Extract the db query
    query = comp.extract_content(res, r'```sql(.*?)```').replace(';', " allow filtering;")
    print(query)
    logging.info(f"Running db query::{query}")

    # Run the query on db and extract the results
    result = db.exe(query)

    # Return the result
    return result


def draft_email(user_input,name='Dorothy'):

    signature = f"Kind regards, \n\{name}"
    context = [
        {"role": "system", "content": f'''You are an assistant who writes emails for the user. 
        You will be asked to draft reply emails. Or emails to convey the things the user wants to convey.
        Your goal is to help the user quickly create a perfect email reply. 
        Start your reply by saying: "Hi, here's a draft for your reply:" And then proceed with the reply on a new line.
        Make sure to sign off with {signature} '''},
        {"role": "user",
         "content": f"{user_input}"}
    ]
    # Initialise ChatResponse object
    comp = Completions()\

    # Generate chat response
    res = comp.generate_response(context)
    logging.info(f"Response::{res}")
    return res

