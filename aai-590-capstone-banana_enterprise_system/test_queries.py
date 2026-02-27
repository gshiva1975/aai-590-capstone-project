import requests
import time
import uuid

API_URL = "http://localhost:8000/analyze"

queries = [
    "Is AAPL a good investment?",
    "Is TSLA overvalued?",
    "What is the outlook for NVDA?",
    "Unknown stock",
    "Is MSFT financially stable?"
]

def send_query(query):
    request_id = str(uuid.uuid4())[:8]
    print("\n" + "=" * 70)
    print(f"[{request_id}] Sending Query: {query}")
    print("=" * 70)

    start = time.time()

    try:
        response = requests.post(API_URL, json={"query": query})
        duration = round(time.time() - start, 3)

        print(f"[{request_id}] Response Time: {duration}s")
        print(f"[{request_id}] Status Code: {response.status_code}")

        data = response.json()

        print("\n--- Response ---")
        print(data)

        if "confidence" in data:
            print(f"\n[{request_id}] Confidence: {data['confidence']}")

    except Exception as e:
        print(f"[{request_id}] ERROR:", str(e))


if __name__ == "__main__":
    print("\n Starting BANANA Query Test\n")

    for q in queries:
        send_query(q)
        time.sleep(1)

    print("\n Completed 5 Query Test\n")

