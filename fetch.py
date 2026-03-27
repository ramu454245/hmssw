import requests
import json

def handler(request):
    try:
        can = request.args.get("can")

        if not can:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "CAN required"})
            }

        TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjkzNzMyNDI5MTYiLCJEZXZpY2VJZCI6IkFQM0EuMjQwOTA1LjAxNS5BMl9WMDAwTDEtdml2by1WMjQzNyIsIm5iZiI6MTc3NDU3ODE0MSwiZXhwIjo0OTMwMjUxNzQxLCJpYXQiOjE3NzQ1NzgxNDF9.7gMfa-3JE7Igf8kz6c3bgspZqDBNSrld64aHU_gE2xw"

        url = "https://local.hyderabadwater.gov.in/HMWSSBAPI/MobileApp/GetConsumerInfoByCAN"

        headers = {
            "Authorization": TOKEN,
            "Content-Type": "application/json",
            "User-Agent": "Dart/3.9 (dart:io)",
            "Accept": "application/json"
        }

        data = {"can": can}

        res = requests.put(url, json=data, headers=headers)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(res.json())
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
