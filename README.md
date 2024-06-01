# PandaMailer-Free

# PandaMailer 🐼

PandaMailer es una herramienta poderosa para el envío masivo de correos electrónicos utilizando Python y la API de MailJet. Ideal para campañas de marketing, newsletters y mucho más. Con PandaMailer, simplemente usa una plantilla CSV con las columnas nombre, correo y link, y deja que nuestro script haga el resto.

## Características

- **Versión 1.0.0**:
  - Envía correos masivos utilizando un archivo CSV.
  - Hasta 6000 correos gratis por mes con MailJet.
  - Hasta 1500 contactos gratis por mes con MailJet.
  - Free

- **Versión 1.0.1**:
  - Seguimiento de aperturas 📬.
  - Visualiza quiénes abren tus correos y optimiza tus campañas.
  - Envía correos masivos utilizando un archivo CSV.
  - Hasta 6000 correos gratis por mes con MailJet.
  - Hasta 1500 contactos gratis por mes con MailJet.
  - Integración Gmail/Gsuit correos y contactos ilimitados.
  - Precio 50 USD
  - Precio implementación no obligatorio : 20 USD

- **Versión 1.1.0**:
  - Seguimiento de aperturas 📬.
  - Visualiza quiénes abren tus correos y optimiza tus campañas.
  - Envía correos masivos utilizando un archivo CSV.
  - Hasta 6000 correos gratis por mes con MailJet.
  - Hasta 1500 contactos gratis por mes con MailJet.
  - Integración Gmail/Gsuit correos y contactos ilimitados
  - ¡Generación de informes en PDF! 📊.
  - Obtén reportes detallados con gráficos y estadísticas de tus envíos.
  - Precio 50 USD
  - Precio implementación no obligatorio: 20 USD

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/pandamailer.git
   cd pandamailer

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

Configuración

1. Crea un archivo .env en el directorio raíz del proyecto con tus credenciales de MailJet:

    ```bash
    MAILJET_API_KEY=tu_api_key
    MAILJET_API_SECRET=tu_api_secret

2. Asegúrate de tener un archivo CSV con la siguiente estructura:

    ```bash
    nombre,correo,url
    John Doe,johndoe@example.com,https://example.com
    Jane Doe,janedoe@example.com,https://example.com

Uso

1. Ejecuta el script principal:

    ```bash
    python pandamailer.py

2. Sigue las instrucciones en la terminal:

  * Envío Manual: Enviar correos inmediatamente.
  * Envío Automático: Programar el envío de correos en lotes con intervalos personalizados.
  * Ver estadísticas de aperturas: Mostrar las estadísticas de quiénes abrieron y hicieron clic en los correos.
  * Generar informe en PDF: Generar un informe detallado en PDF con gráficos y estadísticas.

# *Ejemplo de Uso*

    ```bash
    Selecciona el tipo de envío:
    1. Envío Manual
    2. Envío Automático
    3. Ver estadísticas de aperturas
    4. Generar informe en PDF
      
    Elige una opción (1/2/3/4): 1
    Ingresa la ruta al archivo CSV: path/to/your/file.csv
    Ingresa el asunto del correo: Asunto del Correo
      
    Correo enviado a John Doe <johndoe@example.com>
    Correo enviado a Jane Doe <janedoe@example.com>
    Total de correos enviados: 2

# Contribución
¡Las contribuciones son bienvenidas! Si deseas contribuir a PandaMailer, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -m 'Agregar nueva característica').
Empuja a la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



# **Credits**
Developer: @davenisc
Web: https://davenisc.com

# *Support*
If you find this project useful, you can support me on Buy Me a Coffee.

<a href="https://buymeacoffee.com/davenisc" target="_blank">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee">
</a>

# **Follow Me**

# *Follow me on my social media profiles:*

<a href="https://twitter.com/davenisc" target="_blank">
    <img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
</a>
<a href="https://www.instagram.com/davenisc.co/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a>
<a href="https://www.linkedin.com/in/davenisc/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>

# *Donate USDT* 

If you would like to support this project with a USDT BEP-20 donation, you can send it to the following Binance wallet address:

   ```bash
   0x15283841da6b5099d991fd64fdcb302478f4cc5a
