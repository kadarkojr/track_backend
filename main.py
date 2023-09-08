from fastapi import FastAPI, Query
from datetime import datetime
import json


weekday = datetime.now().strftime('%A')
formatted_datetime_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

app = FastAPI()

@app.get('/api')
async def root(slack_name: str = Query(None, description="slack_name"),
                    track: str = Query(None, description="track")):
    return {
        "slack_name" : slack_name,
        "current_day" : weekday,
        "utc_time": formatted_datetime_str,
        "track" : track,
        "github_file_url" : "https://github.com/kadarkojr/zuri_backend/blob/main/internship/appp.py",
        "github_repo_url" : "https://github.com/kadarkojr/zuri_backend",
        "status_code" : 200

    }