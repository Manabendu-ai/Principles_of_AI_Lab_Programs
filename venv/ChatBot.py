import wikipedia

print("Wikipedia Chatbot")
query = input("Enter your search text: ")

try:
    result = wikipedia.summary(query, sentences=3)
    print("\nInformation from Wikipedia:\n")
    print(result)
except:
    print("No information found on Wikipedia")
