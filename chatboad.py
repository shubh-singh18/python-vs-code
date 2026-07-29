
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JZEGhqoqiSB-D9gTZw6YZHfCrGRPMyaRqW1C7Ec449KQ")

print("Enter 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="models/gemini-3.6-flash",
        contents=user
    )

    print("AI:", response.text)


    