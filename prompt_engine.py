import google.generativeai as genai

gemini_api_key = "AIzaSyDjxwGtkOF5CnQX1SpKE4kbx5u9hOCYYH0"
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")  # Fixed this line

def run_prompt(prompt_type, user_input):
    if prompt_type == "Zero-shot":
        prompt = f"{user_input}"
    elif prompt_type == "Few-shot":
        prompt = (
            "Q. Who is the president of India?\n"
            "A. Ms. Droupadi Murmu\n"
            "Q. Who is the president of the United States?\n"
            "A. Mr. Donald Trump\n"
            f"Q. {user_input}\n"
            "A."
        )
    elif prompt_type == "Instruction-Based":
        prompt = (
            "Instruction : Summarize my article in 3 bullet points.\n"
            f"Text : {user_input}\n"
        )
    elif prompt_type == "Chain-of-Thought":
        prompt = (
            "solve the Neural network backpropagation equation step by step.\n"
            f"Text : {user_input}\n"
        )
    elif prompt_type == "Role-Based":
        prompt = (
            "You are a real estate agent. Tell me why I should buy land in Gurgaon.\n"
            f"Text : {user_input}\n"
        )
    else:
        prompt = user_input

    response = model.generate_content(prompt)
    return response.text  # Fixed this line to return the output
