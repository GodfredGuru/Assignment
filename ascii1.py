def convert_video():
    fn = input("input file name : ")
    hratio = float(input("input height zoom ratio(default 1.0) : ") or "1.0")
    wratio = float(input("input width zoom ratio(default 1.0) : ") or "1.0")
    cap = cv2.VideoCapture(fn)
    i = 0
    if(os.path.isdir("./out") == False):
        os.makedirs("./out")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
             break
        cv2.imshow('image', frame)
        k = cv2.waitKey(5)

        os.system('cls')
        i += 1
        tmp = open('./out/RES('+str(i)+').txt','w')
        frame = cv2.resize(frame, (0,0), fx=wratio, fy=hratio)
        frame = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        trans_data = transform_ascii(frame)
        print(trans_data)
        tmp.write(trans_data)
        tmp.close()

        if (k & 0xff == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows() 
