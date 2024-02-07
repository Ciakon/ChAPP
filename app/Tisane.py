import requests
from tisane_example import example

api_key = "CX1RaJccKqP9IjRKzJsc9C9YzjOWJ1hB"

abuse_types = ["personal_attack", "bigotry", "criminal_activity", "provocation", "data_leak", "profanity"]
min_severity = {"personal_attack" : 0, "bigotry" : 1, "criminal_activity" : 0, "provocation" : 1, "data_leak" : 0, "profanity" : 0}

def fetch_abuse(message) -> list:
    "Returns a list of all instances of abuse in message, in JSON format"

    url = "https://api.apilayer.com/tisane/parse"
    headers = {"apikey" : api_key, "content-type" : "application/json"}
    json = {"language" : "da", "content" : message, "settings" : {"abuse" : True}}

    response = requests.request("POST", url=url, headers=headers, json=json)

    if response.status_code != 200:
        raise Exception(f"tisane api error. error code: {response.status_code}")

    # Returns empty list, if there is no abuse.
    try:
        return response.json()["abuse"]
    except:
        return []

def severity_to_number(severity):
    if severity == "low":
        return 0
    if severity == "medium":
        return 1
    if severity == "high":
        return 2
    if severity == "extreme":
        return 3

def get_abuse(message):
    #TODO remove example
    abuse = fetch_abuse(message)
    #abuse = example["abuse"]
    is_abuse = False
    reasons = []
    
    for item in abuse:
        abuse_type = item["type"]
        severity = severity_to_number(item["severity"])

        if abuse_type in abuse_types:
            if severity >= min_severity[abuse_type]:
                is_abuse = True

                if abuse_type not in reasons:
                    reasons.append(abuse_type)

    return [is_abuse, reasons]
