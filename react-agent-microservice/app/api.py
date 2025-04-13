from fastapi import APIRouter
from app.agent import react_agent

router = APIRouter()

@router.post("/book_restaurant/")
def book_restaurant(request: dict):
    query = request.get("query")
    if not query:
        return {"error": "Query missing."}
    result = react_agent(query)
    return {"result": result}
