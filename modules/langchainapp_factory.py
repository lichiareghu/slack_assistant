from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from config import Config

def draft_email(user_input, name="Lichia"):
    signature = f"Kind regards, \n\{name}"
    template = """

    You are a helpful assistant that drafts an email reply based on an a new email.

    Your goal is to help the user quickly create a perfect email reply.

    Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.

    Start your reply by saying: "Hi {name}, here's a draft for your reply:". And then proceed with the reply on a new line.

    Make sure to sign of with {signature}.

    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=Config.OPENAI_API_KEY)
    chain = ({"user_input": RunnablePassthrough(),
              'name': RunnablePassthrough(),
              'signature': RunnablePassthrough()}
             | prompt
             | model
             | output_parser
             )

    return chain.invoke({"user_input": user_input,
                         'name': name,
                         'signature': signature})

