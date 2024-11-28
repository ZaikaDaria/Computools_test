import json
from typing import List
from app.models import BenchmarkingResult


def load_test_data() -> List[BenchmarkingResult]:
    with open("test_database.json", "r") as file:
        data = json.load(file)

    results = data.get("benchmarking_results", [])
    return [BenchmarkingResult(**result) for result in results]


def calculate_averages(results: List[BenchmarkingResult]) -> dict:
    if not results:
        return {
            "average_token_count": 0.0,
            "average_time_to_first_token": 0.0,
            "average_time_per_output_token": 0.0,
            "average_total_generation_time": 0.0,
        }

    total_count = len(results)
    avg_token_count = sum(result.token_count for result in results) / total_count
    avg_time_to_first_token = sum(result.time_to_first_token for result in results) / total_count
    avg_time_per_output_token = sum(result.time_per_output_token for result in results) / total_count
    avg_total_generation_time = sum(result.total_generation_time for result in results) / total_count

    return {
        "average_token_count": avg_token_count,
        "average_time_to_first_token": avg_time_to_first_token,
        "average_time_per_output_token": avg_time_per_output_token,
        "average_total_generation_time": avg_total_generation_time,
    }
