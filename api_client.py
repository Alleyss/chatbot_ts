from openai import OpenAI
import os


XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",  
)

def get_streaming_chat_response(user_message, conversation_history, temperature=1.0, top_p=None):
    """Streams chat response from the Grok API using OpenAI client with context."""
    messages = [
        {"role": "system", "content": "You are Grok, a helpful chatbot that only responds to code or concept related queries which have streamlit in it. If the query does not relate to streamlit then respond with \"I am not a general chatbot and cannot help with queries that do not relate to Streamlit.\""},
    ]
    # Include last 5 prompts and responses
    for item in conversation_history:
        messages.append(item)

    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="grok-2-1212",
            messages=messages,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        )
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                yield chunk.choices[0].delta.content
        return full_response
    except Exception as e:
        print(f"An error occurred: {e}")
        yield f"An error occurred: {e}"
        return ""

# if __name__ == "__main__":
#     user_input = "Motivate me to getup early"

#     # # Example 1: Default (temperature=1.0)
#     # print("Response with default temperature (1.0):")
#     # get_streaming_chat_response(user_input)

#     # # Example 2: Setting custom temperature
#     # print("\nResponse with temperature = 0.5:")
#     # get_streaming_chat_response(user_input, temperature=0.5)

#     # # Example 3: Setting custom temperature and top_p
#     # print("\nResponse with temperature = 0.7 and top_p = 0.9:")
#     # get_streaming_chat_response(user_input, temperature=0.7, top_p=0.9)

#     # # # Example 4:  Setting temperature (top_p removed)
#     # # print("\nResponse with temperature=0.8")
#     # # get_streaming_chat_response(user_input, temperature=0.8)


#     # # Example 5: Setting temperature and top_p
#     # print("\nResponse with temperature=0.6, top_p=0.8")
#     # get_streaming_chat_response(user_input, temperature=0.6, top_p=0.8)
