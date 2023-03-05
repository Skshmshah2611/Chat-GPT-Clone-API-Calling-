import os
import openai
import gradio as gr


#openai.api_key = os.getenv("OPENAI_API_KEY")


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Your upcoming ride is with the Ai , Please ride carefully \n Click and type your message to Ai :"

def openai_plug(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human :", " AI :"]
    )

    return response.choices[0].text



def chatgpt_nc(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_plug(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>The Ai Ride with GPT-3 Chat BOT </center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_nc, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True , share = True)