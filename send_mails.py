import csv
import requests

# Credenciales de MailJet
MAILJET_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
MAILJET_API_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
MAILJET_API_URL = 'https://api.mailjet.com/v3.1/send'


def enviar_correo(nombre, correo, url, url_python=None):
    auth = (MAILJET_API_KEY, MAILJET_API_SECRET)
    headers = {
        'Content-Type': 'application/json',
    }
    html_part = f'''
                    <html>
                        <head>
                            <style>
                                /* Estilos CSS */
                                body {{
                                    font-family: Arial, sans-serif;
                                }}
                                .container {{
                                    max-width: 600px;
                                    margin: 0 auto;
                                    padding: 20px;
                                    border: 1px solid #ddd;
                                    border-radius: 5px;
                                    text-align: center; /* Centrar contenido */
                                }}
                                .logo {{
                                    width: 70px; /* Forzar dimensiones */
                                    height: 70px;
                                    display: block;
                                    margin: 0 auto; /* Centrar imagen */
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <img src="https://pbs.twimg.com/profile_images/1766099240550318080/xG9NuxRL_400x400.jpg" alt="Logo" class="logo">
                                <p>¡Hola {nombre},!</p>
                                <h3>Soy David Vega y estás recibiendo este correo porque participaste del IV congreso internacional de convergencia tecnológica 2024 realizado por la universidad Areandina.</h3>
                                <p>¡Reclama tu POAP 👉 <a href="{url}">aquí</a> 👈 Es un recuerdo del avento ;)</p>
                                <p>Este correo fue automatizado y enviado con Python 💜</p>
                            </div>
                        </body>
                    </html>
                '''
    if url_python:
        html_part += f'<p>Este correo fue enviado con <a href="{url_python}">Python</a>.</p>'

    data = {
        'Messages': [
            {
                'From': {
                    'Email': 'holamundo@pythonautas.dev',
                    'Name': 'Pythonautas',
                },
                'To': [
                    {
                        'Email': correo,
                        'Name': nombre,
                    }
                ],
                'Subject': 'IV congreso Areandina ¡Reclama tu POAP!',
                'TextPart': f'Hola {nombre}, reclama tu POAP aquí: {url}',
                'HTMLPart': html_part
            }
        ]
    }
    response = requests.post(MAILJET_API_URL, headers=headers, auth=auth, json=data)
    response.raise_for_status()
    print(f'Correo enviado a {nombre} <{correo}>')




# Ruta al archivo CSV
archivo_csv = 'test.csv'
url_python = 'https://python.org'
# Leer el archivo CSV y enviar correos
with open(archivo_csv, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        nombre = row['nombre']
        correo = row['correo']
        url = row['url']
        try:
            enviar_correo(nombre, correo, url)
        except Exception as e:
            print(f'Error al enviar correo a {nombre} <{correo}>: {e}')


