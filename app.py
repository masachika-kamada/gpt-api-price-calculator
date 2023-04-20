import streamlit as st
import json
import tiktoken
from forex_python.converter import CurrencyRates


class APIPricing:
    def __init__(self, model_name):
        self.model_name = model_name
        with open("api_pricing.json", "r") as f:
            data = json.load(f)
        self.prompt_price = float(data[model_name]["prompt_price"])
        self.completion_price = float(data[model_name]["completion_price"])

    def calc_cost(self, text):
        self.text = text
        user_text, assistant_text = self.split_text()
        user_token_count = self.get_token_count(user_text)
        assistant_token_count = self.get_token_count(assistant_text)
        user_cost = user_token_count * self.prompt_price / 1000
        assistant_cost = assistant_token_count * self.completion_price / 1000
        total_cost = user_cost + assistant_cost
        return total_cost

    # split text into USER and ASSISTANT parts
    def split_text(self):
        lines = self.text.split("\n")
        user_text = []
        assistant_text = []
        is_user = True

        for line in lines:
            if line == "## USER":
                is_user = True
                continue
            elif line == "## ASSISTANT":
                is_user = False
                continue
            elif line == "":
                continue

            if is_user:
                user_text.append(line)
            else:
                assistant_text.append(line)

        return " ".join(user_text), " ".join(assistant_text)

    def get_token_count(self, text):
        encoding = tiktoken.encoding_for_model(self.model_name)
        tokens = encoding.encode(text)
        return len(tokens)


def main():
    st.markdown("# GPT API Price Calculator")

    st.markdown("""
    For text input, use the following format to separate user and assistant dialogues:

    * Type "## USER" before the user's dialogue.
    * Type "## ASSISTANT" before the assistant's dialogue.

    For example:
    ```
    ## USER
    Hi, how are you?

    ## ASSISTANT
    I'm doing well, thank you. How can I assist you today?
    ```
    """)

    input_type = st.radio("Input Type", ["Text", "File"])

    if input_type == "Text":
        input_text = st.text_area("Input Text")
    else:
        input_file = st.file_uploader("Input File")

    # model selection
    with open("api_pricing.json", "r") as f:
        data = json.load(f)
    model_names = data.keys()
    selected_model_name = st.selectbox("Select a GPT model", model_names)

    times = st.slider("How many times do you use this service per day?", 1, 100, 10)

    # calculate token count and cost
    if st.button("Calculate"):
        if input_type == "Text":
            text = input_text
        else:
            text = input_file.read().decode("utf-8")

        api_pricing = APIPricing(selected_model_name)
        cost = api_pricing.calc_cost(text)
        monthly_cost = cost * times * 30
        c = CurrencyRates()
        cost_jpy = c.convert("USD", "JPY", cost)
        monthly_cost_jpy = c.convert("USD", "JPY", monthly_cost)

        st.markdown(f"""
        | Cost | Monthly Cost |
        | --- | --- |
        | {cost} USD | {monthly_cost} USD |
        | {cost_jpy} JPY | {monthly_cost_jpy} JPY |
        """)


if __name__ == "__main__":
    main()
