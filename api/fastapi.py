from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/query")
def query_crypto(crypto_name: str = Query(..., description="The name of the cryptocurrency")):
    data = query_crypto_prices(crypto_name)
    if not data:
        return {"error": f"No data found for {crypto_name}"}
    
    analysis = ask_llm(f"Analyze the following data: {data}")
    return {"crypto_name": crypto_name, "analysis": analysis}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Run the FastAPI application
# bash uvicorn main:app --reload
# GET http://127.0.0.1:8000/query?crypto_name=Bitcoin
