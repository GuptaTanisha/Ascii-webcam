import cv2

ascii_chars = [' ','.',':',';','+','*','$','%','S','#','=',":"]
ascii_chars = ascii_chars[::-1]
str = ''

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height = img.shape[0]
    width = img.shape[1]
    aspect_ratio = height/width

    new_width = 120
    new_height = int(aspect_ratio * new_width)

    new_dim = (new_width, new_height)   

    image = cv2.resize(img, new_dim, interpolation = cv2.INTER_AREA)

    for x in range (0,new_height):
        for y in range(0,new_width):
            index = image[x,y]//25
            str = str + ascii_chars[index]
        str = str + "\n"

    print(str)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 