from fastapi import FastAPI


app = FastAPI(title="hello data")


@app.get("/")
def get_items():
 return {"data":"sjkjfd"+" hello gyes"}


@app.get("/items")
def get_items(item:str):
 return {"data":item+" hello gyes"}
