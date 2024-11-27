import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from app.utils import load_test_data, calculate_averages
from app.models import AverageStatistics

app = FastAPI(title="SuperBenchmark API")

SUPERBENCHMARK_DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "true").lower() == "true"


@app.get("/results/average", response_model=AverageStatistics)
async def get_average_statistics():
    if not SUPERBENCHMARK_DEBUG:
        raise HTTPException(status_code=403, detail="Feature not ready for live deployment.")

    results = load_test_data()
    averages = calculate_averages(results)
    return AverageStatistics(**averages)


@app.get("/results/average/{start_time}/{end_time}", response_model=AverageStatistics)
async def get_average_statistics_time_window(start_time: str, end_time: str):
    if not SUPERBENCHMARK_DEBUG:
        raise HTTPException(status_code=403, detail="Feature not ready for live deployment.")

    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Use ISO format.")

    results = load_test_data()
    filtered_results = [
        result for result in results if start <= result.timestamp <= end
    ]

    if not filtered_results:
        raise HTTPException(status_code=404, detail="No results found in the specified time window.")

    averages = calculate_averages(filtered_results)
    return AverageStatistics(**averages)
