import nltk
from nltk.chat.util import Chat, reflections

reflections={
    "i am": "you are",
    "i was": "you were",
    "i": "you ",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "i am",
    "you were":"i was",
    "you've": "i have",
    "you'll": "i will",
    "your":"my",
    "yours":"mine",
    "you":"me",
    "me":"you"
}
pairs=[
    [
        r"my name is (.*)",
        ["Hello %1,How are you"]
    ],
     [
        r"hi|hey|hello",
        ["Hello Hey there!"]
    ],
    [
        r"what is your name",
        ["i am chatbot created by codingal you can call me abc"]
    ], 
    [
        r"how are you",
        ["i am doing good , how about your"]
    ],
      [
        r"i am fine",
        ["great to hear that , how can i help you"]
    ],
    [
        r"i am doing great(.*) ",
        ["Nice to hear that , how can i help you"]
    ],
    
    [
        r"(.*) age",
        ["Nice i am computer programe"]
    ],
    
    [
        r"what (.*) want ",
        ["make me an offer "]
    ],
   [
        r"(.*) created ",
        ["you created me using python"]
    ],
    [
        r"(.*)(location | city)? ",
        ["karachi,islamabad"]
    ],
    [
        r"how is the weather in(.*)? ",
        ["the weather is %1 is awesome"]
    ],
   [
        r"i work in (.*) ?",
        ["%1, is an amzaing company"]
    ],
    [
        r"(.*) raining in (.*) ",
        ["No rain since lastw week"]
    ],
    [
        r"how (.*) health (.*) ",
        ["i am computer program "]
    ],
    [
        r"(.*) (sport|game)? ",
        ["I am  ver big fan of football"]
    ],
    [
        r"who (.*) sportsperson ? ",
        ["Messi" ,"Ranldo" ,"Ronney"]
    ],
    [
        r"i am looking for online guide and courses to leran data science ",
        ["bac_tech has many great articles"]
    ],
    [
        r"quit ",
        ["Bye", "take care"]
    ],
]
def mychat():
    print("hi i am a chatbot ")
    chatbot=Chat(pairs,reflections)
    chatbot.converse()
if__name__ == "__main__": # type: ignore
mychat()
