import requests, time, json

tokens = open('tokens.txt'.strip()).readlines()
print('Reccommended delay is 45-60 seconds')

delay = input('Delay: ')
finished = []

for token in tokens:
    token = token.strip()
    if token not in finished:
        headers = {'authorization': token} # shifting through tokens
        url = 'https://discordapp.com/api/v9/auth/login' # our api endpoint, needed for requesting the validity of the token
        request = requests.post(url, headers=headers) # making the request to the endpoint

        match request.status_code:
            case 200:
                print(f'Token: {token[0:16]} has been validated for your IP')
                with open('output/authenticated.txt', 'a') as authenticated:
                    authenticated.write(f'{token}\n')
                finished.append(token)


            case 429:
                response_json = json.loads(request.text)
                stringlimit = response_json.get('ratelimit')
                ratelimit = float(stringlimit)
                print(f'Sleeping for {ratelimit}')
                
                time.sleep(float(ratelimit))

        time.sleep(int(delay))