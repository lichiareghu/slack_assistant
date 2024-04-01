import json
import re

from config import Config
# from modules.functions_factory import query_database
from typing_extensions import override
import openai
from openai import OpenAI


class EventHandler(openai.AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(end="", flush=True)

    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)

    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)


class ChatWithAssistant:
    def __init__(self):
        """This function will load the assistant id and state variables
        required for continuous contextual chat with the assistant"""
        self.openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.session_state = {"assistant_state": Config.ASSISTANT_ID,
                              "messages": [],
                              "last_openai_run_state": None,
                              "thread_state": self.openai_client.beta.threads.create(),
                              "lock_flag": False}

    def generate_response(self, message, instruction=None, role='user'):
        self.openai_client.beta.threads.messages.create(
            thread_id=self.session_state["thread_state"].id,
            role="user",
            content=message,
            metadata={"role": role}
        )
        # Then, we use the `create_and_stream` SDK helper
        # with the `EventHandler` class to create the Run
        # and stream the response.

        with self.openai_client.beta.threads.runs.create_and_stream(
                thread_id=self.session_state["thread_state"].id,
                assistant_id=self.session_state["assistant_state"],
                instructions=instruction,
                event_handler=EventHandler(),
        ) as stream:
            stream.until_done()

        return stream.get_final_messages()[0].content[0].text.value

    def delete_thread(self):
        # close_chat()
        if self.session_state["thread_state"]:
            self.openai_client.beta.threads.delete(self.session_state["thread_state"].id)


class Completions:
    def __init__(self):
        """This function will load the assistant id and state variables
        required for continuous contextual chat with the assistant"""
        self.openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate_response(self, context):
        """This function will call the completions api
        to generate response for the questions asked"""
        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=context
        )

        # Extract the content of response
        cont = response.choices[0].message.content

        # Return the content
        return cont

    def extract_content(self, input_string, pattern):
        match = re.search(pattern, input_string, re.DOTALL)

        if match:
            return match.group(1)
        else:
            return None
