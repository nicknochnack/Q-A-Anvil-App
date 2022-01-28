from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    def primary_color_1_click(self, **event_args):
        # Access the values from the app 
        question_text = self.question_text.text
        context_text = self.input_text.text

        # Call the jupyter notebook uplink method
        result = anvil.server.call('answer_questions', question_text, context_text)

        # Show the result to the user
        self.answer_text.text = result