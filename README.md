#A python voice controller
PyVoiceControl is a Python based tool used to navigate a computer using only one's voice. With just your voice, you can move the mouse around the screen, click on elements, type characters and navigate programs. This was created at Electric City Hacks 2016.  

Everything was programmed in Python. A simple script was used to handle mouse and keyboard controls. The GUI was created using Tkinter. The speech to text was generated using Google Cloud. The text to speech was generated with MacOS's built in terminal commands. The mouse tracking works by having the user say the text on the screen at which to move the cursor. The text is then search for by taking a screenshot and then running an OCR (with Tesseract) to find the exact locations. Overall, the project is intended as either an assistive program for those who need it, or a simple handy tool.   


##Required tools to run:
-Gcloud  
-PyAudio      
-portaudio  
-tesseract  
-PIL  
-Pillow  
-pyautogui    
-libtif  
-libpng  
-jpeg  
-Tkinter  
-SpeechRecognition  
   
