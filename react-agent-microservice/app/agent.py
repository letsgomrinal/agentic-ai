from app.llm_client import chat
from app.yelp_api import search_restaurants
from app.prompt import SYSTEM_PROMPT

def react_agent(user_query):
    system_prompt = SYSTEM_PROMPT
    context = [
        {
        "role": "system", 
        "content": system_prompt
        }
    ]
    context.append({
        "role": "user", 
        "content": user_query
        }
    )

    for _ in range(5):
        output = chat(context)
        context.append({"role": "assistant", "content": output})

        if "Action:" in output:
            action_line = output.split("Action:")[1].strip().split("\n")[0]
            if action_line.startswith("search_restaurants"):
                query = action_line.split("[")[1].split("]")[0]
                results = search_restaurants(query)
                observation = f"Found {len(results)} options: {results}"
            elif action_line.startswith("book_restaurant"):
                name = action_line.split("[")[1].split("]")[0]
                observation = f"Booking confirmed for {name}."
            else:
                observation = "Unknown action."

            context.append({"role": "user", "content": f"Observation: {observation}"})
        else:
            break

    return output
