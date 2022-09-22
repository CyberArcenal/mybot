import json


def main():
    while True:
        tags=input("tags: ")
        patterns=input("patterns: ")
        response=input("response: ")
        single_response=input("single response?: ")
        requird_words=input("requird words: ")
        save(tags,patterns,response,single_response,requird_words)
def openconfig():
    a=json.loads(open('config.json', 'r').read())
    return a
def config_w(config):
    a=open('config.json', 'w')
    json.dump(config, a)
    a.close()
    return
def save(tags,patterns,response,single_response,requird_words):
    response_storage=[]
    patterns_storage=[]
    patterns=patterns.split()
    requird_words=requird_words.split()
    response_data=response.split()
    single_response=single_response.lower()
    for word in response_data:
        if "_" in word:
            response_storage.append(word.replace('_', ' '))
        else:
            response_storage.append(word)
    for word in patterns:
        if "_" in word:
            patterns_storage.append(word.replace('_', ' '))
        else:
            patterns_storage.append(word)
            
            
    save_json(tags,patterns_storage,response_storage,single_response,requird_words)
def save_json(tags,patterns,response,single_response,requird_words):
    config=openconfig()
    new=True
    for configuration in config:
        if configuration['tags'] == tags:
            new=False
    
    
    if bool(new) == True:
        save_new(tags,patterns,response,single_response,requird_words)
    else:
        save_already(tags,patterns,response,single_response,requird_words)
def save_already(tags,patterns,response,single_response,requird_words):
    config=openconfig()
    for configuration in config:
        if configuration['tags'] == tags:
            for pattern in patterns:
                configuration['patterns'].append(pattern)
            for word in response:
                configuration['response'].append(word)
            for requird_word in requird_words:
                configuration['requird_words'].append(requird_word)
            configuration['single_response']=single_response
    config_w(config)
    print("New configuration save.")
def save_new(tags,patterns,response,single_response,requird_words=[]):
    config=openconfig()
    data={
        "tags": tags,
        "patterns": patterns,
        "response": response,
        "single_response": single_response,
        "requird_words": requird_words
    }
    config.append(data)
    config_w(config)
    print("New configuration save.")
if __name__=="__main__":
    main()
            
                