from fastapi import FastAPI
from pytz import timezone
from datetime import datetime

app = FastAPI()

@app.get("/time/{region}/{city}")
async def time(region: str,city:str):
    timezone = f'{region}/{city}'
    if timezone in pytz.all_timezones:
        tz = pytz.timezone(timezone)
        return { "time": datetime.now(tz) }
