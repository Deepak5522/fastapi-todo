from fastapi import FastAPI

# Create the FastAPI app object
app = FastAPI()

# Define a simple route
@app.get("/")
def read_root():
    return {"Hello": "World"}
