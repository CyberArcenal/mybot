import re, random, json

def probability_test(message, word_patterns, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    for word in message:
        if word in word_patterns:
            message_certainty += 1

 
    percentage = float(message_certainty) / float(len(word_patterns))


    for word in required_words:
        if word not in message:
            has_required_words = False


    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    config=json.loads(open('config.json', 'r').read())
    unknown_response=json.loads(open('unknown.json', 'r').read())
    wordlist = {}
    def response(b_response, list_of_words, single_response=False, required_words=[]):
        nonlocal wordlist
        wordlist[b_response] = probability_test(message, list_of_words, single_response, required_words)


    for reply in config:
        try:
            required_words=reply['required_words']
        except:
            required_words=[]
        response(random.choice(reply['response']), reply['patterns'], bool(reply['single_response']), required_words)


 

    match = max(wordlist, key=wordlist.get)
    #print(wordlist)
    #print(f'Best match = {match} | Score: {wordlist[match]}')

    return random.choice(unknown_response) if wordlist[match] < 1 else match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
