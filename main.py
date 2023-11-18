import requests
from datetime import datetime
import os

QUERY=input("Tell me which exercise ypu did? ")
GENDER='male'
WEIGHT=58
HEIGHT_CM=176
AGE=22

EXERCISE_ENDPOINT=os.environ['EXERCISE_ENDPOINT']
SHEET_ENDPOINT=os.environ['SHEET_ENDPOINT']
APP_ID=os.environ['APP_ID']
APP_KEY=os.environ['APP_KEY']
TOKEN=os.environ['TOKEN']

parameters={
    "query":QUERY,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT_CM,
    "age":AGE,
}

heders={
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,    
}

response=requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=heders)
print(response.status_code)
exercise_data=response.json()
print(exercise_data)
exercises=[exercise for exercise in exercise_data["exercises"]]
print(exercises)

current_date=datetime.now().date().strftime('%d/%m/%Y')
current_time=datetime.now().time().strftime("%H:%M:%S")


sheet_response=requests.get(url=SHEET_ENDPOINT)
print(sheet_response.json())

bearer_headers={
    "Authorization": f"Bearer {TOKEN}",
}

for exercise in exercises:
    workout_params={
        "workout":{
            "date":f"{current_date}",
            "time":f"{current_time}",
            "exercise":f"{exercise['name']}",
            "duration":f"{exercise['duration_min']}",
            "calories":f"{exercise['nf_calories']}",

        }
    }
    print(workout_params)
    post_response=requests.post(url=SHEET_ENDPOINT, json=workout_params, headers=bearer_headers)
    print(post_response)
