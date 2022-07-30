from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title='Personal Travel Planner',
    description='This personal travel planner will help you scheduler your travel by showing the weather for departure and return date'
)

@app.get('/health-check')
def health_check():
    return {'message': 'FastAPI it\'s working'}

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse('/docs')
