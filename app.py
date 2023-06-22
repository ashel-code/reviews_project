"""Server file"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from predict import predict


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware, 
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = methods,
#     allow_headers = headers    
# )


@app.post("/")
async def process_list(my_list: dict):
    """
    Function that provides all server interaction
    :param my_list: List of reviews from Google extension
    :return: List of analysed reviews
    """
    # Assuming the input is a JSON object with a "list" key containing the list
    data = my_list["list"]
    input_list = data

    return {"result": predict(input_list)}


if __name__ == "__main__":
    # Run server
    port = int(os.environ.get('PORT', 8000))
    run(app, host="0.0.0.0", port=port)
