import requests

url = 'https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed'
headers = {
        'Accept': 'application/json;text/xml',
        'Content-Type': 'audio/wav; codec=audio/pcm; samplerate=16000',
        'Ocp-Apim-Subscription-Key': '171fdfef86c54a9c963f922375c298c7',
        'Host': 'speech.platform.bing.com',
        'Transfer-Encoding': 'chunked',
        'Expect': '100-continue'
        }

r = requests.post(url, data = file('output.wav','rb').read(), headers=headers)
print(r)
