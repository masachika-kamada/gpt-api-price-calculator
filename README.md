# GPT API Price Calculator

This is a Streamlit web application that allows you to calculate the cost of using OpenAI's GPT API based on the amount of text you input and the selected GPT model.

You can access the web application at the following URL: <https://gpt-api-price-calculator.streamlit.app/>

## Input Format

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

## API Pricing

Here's a reference pricing for the available GPT models:

| Model | Prompt Price (USD / 1K tokens) | Completion Price (USD / 1K tokens) |
| :--- | :---: | :---: |
| gpt-3.5-turbo | 0.002 | 0.002 |
| gpt-4-8k | 0.03 | 0.06 |
| gpt-4-32k | 0.06 | 0.12 |

## How to use

0. Visit <https://gpt-api-price-calculator.streamlit.app/>
1. Select the input type, either "Text" or "File"
2. If you choose "Text" input, enter the text in the provided text area. Otherwise, upload a file.
3. Select the desired GPT model from the dropdown menu.
4. Use the slider to indicate how many times you plan to use the service per day.
5. Click the "Calculate" button.

## Output

The application will output a table that shows the cost and monthly cost of using the selected GPT model based on the input text and usage frequency.

The cost will be shown in USD and JPY. The currency conversion rate is based on the current exchange rate from USD to JPY using the `forex-python` package.

## Conclusion

I hope this helps in understanding how to use the GPT API Price Calculator and the associated API pricing. Feel free to try out the web application and provide feedback if you have any suggestions for improvement.
