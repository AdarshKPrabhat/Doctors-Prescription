class final:

    def startRecord(self):
        import pyaudio
        import wave
        FORMAT = pyaudio.paInt16 # data type formate
        CHANNELS = 2 # Adjust to your number of channels
        RATE = 44100 # Sample Rate
        CHUNK = 1024 # Block Size
        RECORD_SECONDS = 20 # Record time
        WAVE_OUTPUT_FILENAME = "file.wav"

        # Startup pyaudio instance
        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        print ("recording...")
        frames = []

        # Record for RECORD_SECONDS
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print ("finished recording")


        # Stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Write your new .wav file with built in Python 3 Wave module
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        
    def convert_to_text(self):

        import speech_recognition as sr
        sound = "file.wav"
    
        r = sr.Recognizer()
    
    
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
    
    
            print("Converting Audio To Text ..... ")
    
    
            audio = r.listen(source)
    
    
    
        try:
            print("Converted Audio Is : \n" + r.recognize_google(audio))
    
    
        except Exception as e:
            print("Error {} : ".format(e) )

    def text_filtration(self):

        
        keyword=["Name","Symptoms","Diagnosis","prescription","advice"]

        f = open('C:\\voice_prescription\\textres.txt', 'r')
        final = []
        for i in f.readlines():
            temp = list(i.split())
            
            for j in temp:
                final.append(j)
        f.close()
        print(final)


        for i in range(0,len(final)):
            if final[i] == "Name":
                
                text =""

                while True:
                    text += " " + final[i]
                    i+=1
                    if i==len(final):
                        file1 = open("Name.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    if final[i] in keyword:
                        
                        # Opening and Closing a file "MyFile.txt" 
                        # for object name file1. 
                        file1 = open("Name.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    
                        

        
            
            if final[i] == "Diagnosis":
                text =""

                while True:
                    text += " " + final[i]
                    i+=1
                    if i==len(final):
                        file1 = open("Diagnosis.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    if final[i] in keyword:
                        
                        # Opening and Closing a file "MyFile.txt" 
                        # for object name file1. 
                        file1 = open("Diagnosis.txt","w")
                        file1.write(text)
                        file1.close()
                        break
            if final[i] == "Symptoms":
                text =""

                while True:
                    
                    text += " " + final[i]
                    i+=1
                    if i==len(final):
                        file1 = open("Symptoms.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    if final[i] in keyword:
                        
                        # Opening and Closing a file "MyFile.txt" 
                        # for object name file1. 
                        file1 = open("Symptoms.txt","w")
                        file1.write(text)
                        file1.close()
                        break
            if final[i] == "prescription":
                text =""
                
                while True:
                    print(text)
                    text += " " + final[i]
                    i+=1
                    if i==len(final):
                        file1 = open("prescription.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    if final[i] in keyword:
                    
                        # Opening and Closing a file "MyFile.txt" 
                        # for object name file1. 
                        file1 = open("prescription.txt","w")
                        file1.write(text)
                        file1.close()
                        break
            if final[i] == "advice":
                text =""

                while True:
                    text += " " + final[i]
                    i+=1
                    if i==len(final):
                        file1 = open("advice.txt","w")
                        file1.write(text)
                        file1.close()
                        break
                    
                    if final[i] in keyword:
                        
                        # Opening and Closing a file "MyFile.txt" 
                        # for object name file1. 
                        file1 = open("advice.txt","w")
                        file1.write(text)
                        file1.close()
                        break

    def text_separation(self):
        import io 
        from nltk.corpus import stopwords 
        from nltk.tokenize import word_tokenize 
        #word_tokenize accepts a string as an input, not a file.
        keyword=["Name","Symptoms","Diagnosis","prescription","advice"]
        for i in range(0,len(keyword)):
            stop_words = set(stopwords.words('english')) 
            file1 = open(keyword[i]+".txt") 
            line = file1.read()# Use this to read file content as a stream: 
            words = line.split() 
            for r in words: 
                if not r in stop_words: 
                    appendFile = open('filtered'+keyword[i]+'.txt','w') 
                    appendFile.write(" "+r) 
                    appendFile.close() 

    
    def generate_text(self,final):
        for i in range(0,len(final)):
                if final[i] == "Name" or final[i] == "name":
                        i+=1
                        textname =""
                        while True:
                                textname += " " + final[i]
                                i+=1
                                if i==len(final):
                                        return textname
                                        break
                if final[i] == "Symptoms" or final[i] == "symptoms":
                        i+=1
                        textsymptoms =""
                        while True:
                                textsymptoms += " " + final[i]
                                i+=1
                                if i==len(final):
                                        return textsymptoms
                                        break
                if final[i] == "Diagnosis" or final[i] == "diagnosis":
                        i+=1
                        textDiagnosis =""
                        while True:
                                textDiagnosis += " " + final[i]
                                i+=1
                                if i==len(final):
                                        return textDiagnosis
                                        break
                if final[i] == "prescription" or final[i] == "Prescription":
                        i+=1
                        textprescription =""
                        while True:
                                textprescription += " " + final[i]
                                i+=1
                                if i==len(final):
                                        return textprescription 
                                        break
                if final[i] == "advice" or final[i] == "advice":
                        i+=1
                        textadvice =""
                        while True:
                                textadvice += " " + final[i]
                                i+=1
                                if i==len(final):
                                        return textadvice 
                                        break

        
    def merged_file(self):

        keyword=["Name","Symptoms","Diagnosis","prescription","advice"]
        answer = []    
        fh = open('merged.txt', 'a')             
        for i in range(0,len(keyword)):
            f = open('filtered'+keyword[i]+'.txt', 'r+')
            f
            final = []
            for i in f.readlines():
                    temp = list(i.split())
                    for j in temp:
                            final.append(j)
            f.close()
            ans = self.generate_text(final)
            answer.append(ans)
        for  i in answer:
            fh.write(i+"\n")
        return answer

    def google_translate(self):
        import googletrans
        
        from googletrans import Translator

        file_translate = Translator()

        f = open("merged.txt", 'r')

        contents = f.read()

        f.close()



        result = file_translate.translate(contents, src='en', dest='mr')

        f = open("text2.txt", "a")

        f.write(result.text)

        f.close()

    def pdfgene(self):

        keyword=["Name","Symptoms","Diagnosis","prescription","advice"]

                    # Import FPDF class
        from fpdf import FPDF
        
        # Create instance of FPDF class
        # Letter size paper, use inches as unit of measure
        pdf=FPDF(format='letter', unit='in')
        
        # Add new page. Without this you cannot create the document.
        pdf.add_page()
        
        # Remember to always put one of these at least once.
        pdf.set_font('Times','B',10.0) 
        
        # Effective page width, or just epw
        epw = pdf.w - 2*pdf.l_margin
        
        # Set column width to 1/4 of effective page width to distribute content 
        # evenly across table and page
        col_width = epw/2
        
        # Since we do not need to draw lines anymore, there is no need to separate
        # headers from data matrix.
        resarray  = self.merged_file()

        data = [['keywords','Values'],
        ['Name',resarray[0]],
        ['Symptoms',resarray[1]],[
        'Diagnosis',resarray[2]],
        ['Prescription',resarray[3]],
        ['advice',resarray[4]]]

        # Text height is the same as current font size
        th = pdf.font_size
        
        # Line break equivalent to 4 lines
        pdf.ln(4*th)
        
        pdf.set_font('Times','B',14.0) 
        pdf.cell(epw, 0.0, 'Doctors Prescription', align='C')
        pdf.set_font('Times','B',10.0) 
        pdf.ln(0.5)
        
        # Here we add more padding by passing 2*th as height
        for row in data:
            for datum in row:
                # Enter data in colums
                pdf.cell(col_width, 2*th, str(datum), border=1)
        
            pdf.ln(2*th)
        
        pdf.output('table-using-cell-borders.pdf','F')

                        
                





    
    




            
e = final()
#e.startrecord()
e.convert_to_text()
#e.text_filtration()
#e.text_separation()
#e.merged_file()
#e.google_translate()
#e.pdfgene()





    
