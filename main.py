from fastapi import FastAPI
import json
app = FastAPI()
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")

def hello():
    return {"message": "Patients management system app"}

@app.get("/about")
def about():
    return {"message": "fully functional api to manage your patients records"}

@app.get("/view")
def view():
    data = load_data()

    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')