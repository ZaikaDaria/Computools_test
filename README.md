# SuperBenchmark API

SuperBenchmark API is a FastAPI-based application designed to manage and query benchmarking results for a Large Language Model (LLM). It allows users to calculate average performance statistics across benchmarking results and filter them by time windows.

---

## **Features**

- **GET `/results/average`**: Retrieve average statistics across all benchmarking results.
- **GET `/results/average/{start_time}/{end_time}`**: Retrieve average statistics for benchmarking results within a specified time window.
- Built-in support for **DEBUG mode** that loads data from a `test_database.json` file.
- Data validation using **Pydantic** models.

---


## **API Endpoints**

### 1. **GET `/results/average`**
Returns average performance statistics for all benchmarking results.

#### **Example Response:**
```json
{
    "average_token_count": 10.2,
    "average_time_to_first_token": 216.0,
    "average_time_per_output_token": 27.6,
    "average_total_generation_time": 485.2
}
```

### 2. **GET `/results/average/{start_time}/{end_time}`**
Returns average performance statistics for benchmarking results within the specified time window.

Path Parameters:

+ **`start_time:`** Start of the time window in ISO format (**`YYYY-MM-DDTHH:MM:SS`**).
+ **`end_time:`** End of the time window in ISO format (**`YYYY-MM-DDTHH:MM:SS`**).

Example Request:

```
GET /results/average/2024-06-01T12:00:00/2024-06-02T11:00:00
```

Example Response:


```json
{
    "average_token_count": 8.5,
    "average_time_to_first_token": 180.0,
    "average_time_per_output_token": 25.5,
    "average_total_generation_time": 500.0
}
```

## Setup Instructions:

1. Clone the repository

```
git clone <repository_url>
cd SuperBenchmark
```

2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Add environment variables

Create a .env file in the project root and add the following line:

```
SUPERBENCHMARK_DEBUG=true
```

5. Run the server

```
uvicorn app.main:app --reload
```

6. Test the API

+ Swagger Documentation: http://127.0.0.1:8000/docs
+ ReDoc Documentation: http://127.0.0.1:8000/redoc
