import pyttsx3
import speech_recognition as sr
import openai

engine = pyttsx3.init()
recognizer = sr.Recognizer()
api_key = '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'

def ask_openai(question):
    client = openai.API(api_key=api_key)  
    chat_completion = client.Chat.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo-1106",
    )
    return chat_completion.choices[0].message.content.strip()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def main():
    print("Hello! I'm your virtual assistant.")
    while True:
        print("Select an option:")
        print("1. Type your question")
        print("2. Speak your question")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            user_input = input("You: ")
        elif choice == '2':
            user_input = speech_to_text()
        elif choice == '3':
            print("Hiya: Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if user_input.lower() == 'bye':
            print("Hiya: Goodbye!")
            break
        response = ask_openai(user_input)
        print("Hiya:", response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
