import PyPDF2
import pyttsx3

filename = input('Digite o nome do arquivo pdf incluindo a extensão: ').strip()

try:
  with open(filename, 'rb') as pdf:
    # Create PdfFileReader
    reader = PyPDF2.PdfReader(pdf)
    # Get an engine instance for the speech synthesis
    speak  = pyttsx3.init()
    # Iterate each page and read the text
    for page_num in range(len(reader.pages)):
      page = reader.pages[page_num]
      text = page.extract_text()
      if text:
        speak.say(text)
        speak.runAndWait()

    # Stop the speech engine
    speak.stop()

    print('Criação do audiobook finalizada')
except FileNotFoundError:
  print('Arquivo não encontrado')
except Exception as e:
  print(f'Um erro ocorreu: {e}')