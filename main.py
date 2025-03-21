import os
import requests
from datetime import datetime, timedelta
import concurrent.futures
import time


def download_image(date):
    year = date.strftime("%Y")
    mmdd = date.strftime("%m%d")

    # URL format based on the example
    url = f"http://img.owspace.com/Public/uploads/Download/{year}/{mmdd}.jpg"

    # Create target directory
    save_dir = f"./img/{year}"
    os.makedirs(save_dir, exist_ok=True)
    save_path = f"{save_dir}/{mmdd}.jpg"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Save the image
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {url}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False


def main():
    # Get configuration from environment variables with defaults
    start_date_str = os.environ.get("START_DATE", "2015-02-18")
    end_date_str = os.environ.get("END_DATE", "2025-12-31")
    max_workers = int(os.environ.get("MAX_WORKERS", "20"))

    # Parse date strings
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError as e:
        print(f"Error parsing dates: {e}")
        print("Date format should be YYYY-MM-DD")
        return

    print(f"Date range: {start_date_str} to {end_date_str}")
    print(f"Starting concurrent download with {max_workers} workers")

    # Generate all dates
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)

    # Use ThreadPoolExecutor for concurrent downloads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all download tasks
        future_to_date = {executor.submit(download_image, date): date for date in dates}

        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_date):
            date = future_to_date[future]
            try:
                success = future.result()
                if not success:
                    print(f"Failed to download image for {date.strftime('%Y-%m-%d')}")
            except Exception as e:
                print(f"Error processing {date.strftime('%Y-%m-%d')}: {e}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Download completed in {time.time() - start_time:.2f} seconds")