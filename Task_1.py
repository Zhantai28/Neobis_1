import json

my_info = {
    "first name": "Zhantai",
    "last name": "Ismailov",
    "age": 20,
    "Email": "Zhantai.Ismailov@gmail.com",
    "Phone number": "+996 702-00-79-90",
    "city": "Bishkek",
    "university": "Girne American University",
    "place of work": "Lego robotics teacher",
    "family": [
        {
            "first name": "Islam",
            "age": 14
        },
        {
            "first name": "Begimay",
            "age": 18
        },
        {
            "first name": "Tagay",
            "age": 2
        }
    ],
    "favorites": [
        {
            "Favorite Anime": ["Death note", "Naruto", "Attack on Titan"]
        },
        {
            "Favorite Movie": ["The Shawshank redemption", "Knives Out", "Catch Me If You Can"]
        },
        {
            "Favorite dishes": ["Manty", "Samsa", "Shawarma", "Pizza"]
        }
    ]
}

with open("My_info.json", 'w') as write_file:
    json.dump(my_info, write_file, indent=4)
