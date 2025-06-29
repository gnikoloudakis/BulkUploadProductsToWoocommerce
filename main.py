import os

from dotenv import load_dotenv

from products import products

load_dotenv()
import requests

# Replace with your site and credentials
url = "https://cranky.cranky.gr/wp-json/wc/v3/products"
image_url = "https://cranky.cranky.gr/wp-content/uploads/2025/06"
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
failures = []
# Bulk upload
for product in products:
    # ✅ ADDED: Check if product already exists by name
    search_url = f"{url}?search={product['name']}"
    search_response = requests.get(search_url, auth=(consumer_key, consumer_secret))
    if search_response.status_code == 200:
        existing = search_response.json()
        if existing:
            print(f"❗ Product already exists: {existing[0]['id']} — {existing[0]['name']}")
            continue

    # 🔄 MODIFIED: only create if product doesn't exist
    response = requests.post(url, auth=(consumer_key, consumer_secret), json=product)
    if response.status_code != 201:
        failures.append(product['name'])
        print(f"❌ Failed to create product: {product['name']}")
        print(response.text)
        continue
    print(response.status_code)
    print(response.text)

    if response.headers.get("content-type") == "application/json":
        data = response.json()
        print(f"✅ Created: {data.get('name')} (ID: {data.get('id')})")
    else:
        print("⚠️ Response is not JSON:", response.text)
# Print failures
if failures:
    print("❗ Failed to create the following products:")
    for name in failures:
        print(f"- {name}")
