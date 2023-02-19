import requests, uuid, json
from fpdf import FPDF 
import os


def translatorit(data,to,translate_path):
    
    
    key = os.getenv('KEY_AZURE_TRANSLATE')
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    location = "westeurope"
    path = '/translate'
    constructed_url = endpoint + path
    params = {
        'api-version': '3.0',
        'to': to
    }
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    # body = [{
    #     'text': 'I would really like to drive your car around the block a few times!'
    # }]
    body = [{'text': data}]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    # a = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    if len(to) <= 1:
        _lang = f'-{to[0]}.text'
        __translate_path = translate_path.replace('.text',_lang).replace('.txt',_lang).replace('.word',_lang)
        _res = response[0]['translations'][0]['text']
        with open(__translate_path, 'w') as f:
                f.write(_res)
    else:
        for i in range(len(to)):
            res = response[0]['translations'][i]['text']
            lang = to[i]
            lang = f'-{lang}.text'
            _translate_path = translate_path.replace('.text',lang).replace('.txt',lang).replace('.word',lang)
            with open(_translate_path, 'w') as f:
                f.write(res)
            

        
        
        
    
