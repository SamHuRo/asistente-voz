#Librerias a importar
import pyttsx3
#import gtts
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Escuchar por el microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #Almacenar recognizer en variable
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as origen:
        #Tiempo de espera
        r.pause_threshold = 0.8

        #Informar que se comenzo la grabacion
        print("Ya puedes hablar")

        #Guardar audio
        audio = r.listen(origen)

        try:
            #Buscar en google lo que esucho
            pedido = r.recognize_google_cloud(audio, lenguage="en-US")
            #Prueba
            print("Digiste: ", pedido)
            
            return pedido
        except sr.UnknownValueError:
            #Prueba
            print("UPS!! No entendi")

            return "Sigo esperando"
        except sr.RequestError:
            #Prueba
            print("UPS!! No hay servicio")

            return "Sigo esperando"
        except:
            #Prueba
            print("UPS!! Algo salio mal")

            return "Sigo esperando"


#Utilizar funcion
transformar_audio_en_texto()