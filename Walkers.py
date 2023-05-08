import cv2


# Crie nosso classificador de corpos

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    bodygray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    
    # Passe o quadro para nosso classificador de corpos
    body = body_classifier.detectMultiScale(bodygray, 1.1, 5)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for(x,y,w,h) in body:
        cv2.rectangle(cap,(x,y),(x+w, y+h), (180,255,0), 2)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break
    cv2.imshow("Janela", cap)
cap.release()
cv2.destroyAllWindows()
