import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def make_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        return f"Request failed: {e}"

def stress_test(url, num_requests):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(make_request, url) for _ in range(num_requests)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    url = input("Enter the URL to stress test (e.g., http://localhost:8000): ")
    num_requests = int(input("Enter the number of requests to make: "))
    stress_test(url, num_requests)