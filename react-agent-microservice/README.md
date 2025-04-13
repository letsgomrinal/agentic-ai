# ReAct Agent

- Create virtual env

```
python -m venv testenv
```

- Activate virtual env

```
source  testenv/bin/activate
```

# Yelp API:

- Get developer Access ![here](https://www.yelp.com/developers/v3/manage_app)

- export API key

```
export YELP_API_KEY=<your yelp api key>
```

- Sample response:
```bash
[
    {'name': 'Robba da Matti', 'rating': 4.2, 'address': '1127 Mainland Street'}, 
    {'name': "Zefferelli's", 'rating': 4.2, 'address': '1136 Robson Street'}, 
    {'name': 'Lupo', 'rating': 4.3, 'address': '869 Hamilton Street'}, 
    {'name': 'Nook', 'rating': 4.2, 'address': '781 Denman Street'}, 
    {'name': 'Ask For Luigi', 'rating': 4.1, 'address': '305 Alexander Street'}
]
```


- Running it locally:

```
uvicorn main:app --reload
```

- API Endpoint:

```
POST http://localhost:8080/book_restaurant/
Body:
{
  "query": "Find a great Italian restaurant nearby and book a table."
}
```