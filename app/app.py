from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import ValidationError
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.config import settings
from app.api.api_v1.router import router

app = FastAPI(
    title='Personal Travel Planner',
    description=settings.APP_DESCRIPTION,
    version='0.1.0',
    swagger_ui_parameters={'defaultModelsExpandDepth': -1}
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail':exc.errors()})
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({'detail':exc})
    )


@app.get('/health-check', tags=['DEFAULT'])
def health_check():
    return {'message': 'FastAPI it\'s working'}

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse('/docs')

app.include_router(router, prefix=settings.API_V1)