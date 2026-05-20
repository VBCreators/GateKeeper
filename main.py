import fastapi

count = 0


app = fastapi.FastAPI()

@app.get("/")
def read_root():
    count += 1
    return {"Hello": f"{count}"}


