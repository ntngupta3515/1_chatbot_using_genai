import panel as pn

class GUI:
    def __init__(self, ai) -> None:
        
        # Initialize Stuff
        pn.extension() # Initializes JS for the GUI
        self.panels = [] # Collect display panels
        self.context = [] # Collects the context for the chatbot
        self.ai = ai # Initializes the AI

        # Initialize the input field
        self.inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…', sizing_mode="stretch_width")

        # Initialize the button to send the data
        self.button_conversation = pn.widgets.Button(name="Chat")

        # Bind the button to the function that collectrs the panels to display
        interactive_conversation = pn.bind(self.collect_messages, self.button_conversation)

        # Display stuff
        dashboard = pn.Column(

            # First display the conversation
            pn.panel(interactive_conversation, loading_indicator=True, sizing_mode="stretch_width"),

            # Then display the input button with the send button
            pn.Row(self.inp, self.button_conversation, sizing_mode="stretch_width"),
            sizing_mode="stretch_both"
        )
        pn.serve(dashboard)

    def collect_messages(self, _):
        prompt = self.inp.value_input
        self.inp.value = ''
        self.context.append({'role':'user', 'content':f"{prompt}"})
        response = self.ai.runMessages(self.context) 
        self.context.append({'role':'assistant', 'content':f"{response}"})
        self.panels.append(pn.Row('User:', pn.pane.Markdown(prompt, sizing_mode="stretch_width")))
        self.panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, styles={'background-color': '#F6F6F6'}, sizing_mode="stretch_width")))    
        return pn.Column(*self.panels, sizing_mode="stretch_width")
