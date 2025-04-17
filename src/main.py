from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
import requests

app = FastAPI()

MOCKOON_CONTACTS_URL = "http://localhost:4001/contact_validation"

class Contact(BaseModel):
    name: str
    email: EmailStr

@app.post("/create_contact", status_code=status.HTTP_201_CREATED)
def create_contact(contact: Contact):
    try:
        response = requests.post(MOCKOON_CONTACTS_URL, json={"email": contact.email})
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="No se pudo contactar con el servicio de validación.")

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Error en el servicio externo de validación.")

    result = response.json()

    if result.get("allowed") is True:
        return {"message": "Contacto creado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="El contacto no está permitido")