from twilio.rest import Client

# Credenciales de Twilio
account_sid = 'US439f9f9523299603a83c665e1137f234'
auth_token = 'A8QD6QL6Y1LXLW3G1G3C1T1K'
client = Client(account_sid, auth_token)

# Configuración del mensaje
from_whatsapp_number = 'whatsapp:+14155238886'  # Número de Twilio para WhatsApp
to_whatsapp_number = 'whatsapp:+593999933388'  # Número de destino

# Enviar mensaje
message = client.messages.create(
    body='¡Hola! Este es un mensaje enviado desde Python usando Twilio.',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"Mensaje enviado con SID: {message.sid}")