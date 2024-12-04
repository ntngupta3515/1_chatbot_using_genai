import panel as pn

class GUI:
    def __init__(self, contextBuilder) -> None:
        
        # Initialize Stuff
        pn.extension() # Initializes JS for the GUI
        self.panels = [] # Collect display panels
        self.contextBuilder = contextBuilder # Initializes the context builder

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

        # Get the user input
        prompt = self.inp.value_input

        # reset it
        self.inp.value = ''

        # Add the context and get the latest response
        self.contextBuilder.add(prompt)
        response = self.contextBuilder.getLastResponse()

        # Append it to display panels and return it
        self.panels.append(pn.Row('User:', pn.pane.Markdown(prompt, sizing_mode="stretch_width")))
        self.panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, styles={'background-color': '#F6F6F6'}, sizing_mode="stretch_width")))    
        return pn.Column(*self.panels, sizing_mode="stretch_width")
