import json

TAGS_MAPPING = {
    "1": "Greetings",
    "2": "Goodbye",
    "3": "FAQ",
    "4": "Help",
    "5": "Orders",
    "6": "Product Information",
    "7": "Payments",
    "8": "Travel",
    "9": "News",
    "10": "Weather",
    "11": "Entertainment",
    "12": "Health",
    "13": "Customizations",
    "14": "Technical Support",
    "15": "General Inquiries"
}

def main():
    while True:
        tags = get_tag()
        patterns = get_patterns()
        response = get_response()
        single_response = input("single response? [Y/n]: ").lower()
        required_words = get_required_words()
        
        if single_response.lower() == "y":
            single_response = True
        else:
            single_response = False
            
        save(tags, patterns, response, single_response, required_words)

def get_required_words():
    while True:
        try:
            response = input("required words: ").split()
            print(f"Required words patterns: {response}")
            return response
        except Exception as e:
            print(e)
            
def get_response():
    while True:
        try:
            response = input("Response: ").split()
            print(f"Response patterns: {response}")
            return response
        except Exception as e:
            print(e)

def get_patterns():
    while True:
        try:
            patterns = input("Chat patterns: ").split()
            print(f"Sender patterns: {patterns}")
            return patterns
        except Exception as e:
            print(e)
            
def get_tag():
    print("Tags:")
    for key, value in TAGS_MAPPING.items():
        print(f"{key}. {value}")
    
    tags = input("Enter the tag number: ")
    return TAGS_MAPPING.get(tags, "General Inquiries")

def openconfig():
    try:
        with open('data/config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def config_w(config):
    with open('data/config.json', 'w') as file:
        json.dump(config, file)

def save(tags: str, patterns: list, response: list, single_response: bool, required_words: list):
    patterns_storage = patterns
    required_words = [word.replace('_', ' ') if "_" in word else word for word in required_words]
    response_storage = [word.replace('_', ' ') if "_" in word else word for word in response]
    patterns_storage = [word.replace('_', ' ') if "_" in word else word for word in patterns_storage]
    save_json(tags, patterns_storage, response_storage, single_response, required_words)

def save_json(tags, patterns, response, single_response, required_words):
    config = openconfig()
    is_new = tags not in config

    if is_new:
        save_new(tags, patterns, response, single_response, required_words)
    else:
        save_already(tags, patterns, response, single_response, required_words)

def save_already(tags: str, patterns: list, response: set, single_response: bool, required_words: list):
    config = openconfig()
    configuration = config.get(tags, {"patterns": [], "response": [], "required_words": [], "single_response": single_response})
    configuration['patterns'].extend(patterns)
    configuration['response'].extend(response)
    configuration['required_words'].extend(required_words)
    configuration['single_response'] = single_response

    config[tags] = configuration
    config_w(config)
    print("Existing configuration updated.")

def save_new(tags, patterns, response, single_response, required_words=[]):
    config = openconfig()
    data = {
        "patterns": patterns,
        "response": response,
        "single_response": single_response,
        "required_words": required_words
    }
    config[tags] = data
    config_w(config)
    print("New configuration saved.")

if __name__ == "__main__":
    main()
