import requests
import xmltodict
import json

url = "https://ibandce.com.br/wp-json/wp/v2/ceara"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Substituir ou remover caracteres inválidos
    for post in data:
        if 'yoast_head_json' in post:
            twitter_misc = post['yoast_head_json'].get('twitter_misc', {})
            if "Est. tempo de leitura" in twitter_misc:
                tempo_leitura = twitter_misc.pop("Est. tempo de leitura")
                twitter_misc["Est_tempo_de_leitura"] = tempo_leitura

    wrapped_data = {"root": {"@xmlns:wp": "https://wordpress.org/ns/", "post": data}}

    # Geração do XML com codificação utf-8
    xml_data = xmltodict.unparse(wrapped_data, pretty=True, encoding='utf-8')

    # Salvar o XML em um arquivo
    with open('dados_convertidos.xml', 'w', encoding='utf-8') as file:
        file.write(xml_data)

    print("XML gerado com sucesso!")

else:
    print("Erro ao buscar os dados.")
