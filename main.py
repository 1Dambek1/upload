from fastapi import FastAPI


app = FastAPI(title="hello data")



@app.get("/items")
def get_items(item:str):
 return {"data":item+" hello gyes"}
