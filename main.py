# Import socket module
from datetime import date
from socket import *  #
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))
# Listen to at most 1 connection at a time
serverSocket.listen(1)
print("The server is ready to receive")
# Server should be up and running and listening to the incoming connections
flage=1#check if page end with html is it main page
while True:
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(addr)# print the address
    print(sentence)



    ip = addr[0]
    port = addr[1]



    request = sentence.split()[1]
    m=sentence.split()[1]
    m2=m.split('.')[0]
    myF=m2.split('/')[1]# get the file name

    print("***")

    print("The Request")
    print(request)
    print("***")
    # to get index without HTTP
    if request== "/index.html" or request== "/":# if the request was index.html or empty it will return the main.html file
        flage = 0# if the request done make the flage false
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filex = open("main.html", "rb")
        connectionSocket.send(filex.read())
        connectionSocket.close()

    elif request.endswith('.html') :# if the request was end with .html return html file
        if (flage==0):# if we entered the previous request continue from the next if statment
            continue
        elif(flage==1):
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            filex = open(myF+".html", "rb")
            connectionSocket.send(filex.read())
            connectionSocket.close()

    elif request.endswith('.png'):
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())

        connectionSocket.send("\r\n".encode())
        s = open(myF+".png", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())
        connectionSocket.close()


    # Send the content of the requested 3 file to the client
    # when enter http://localhost:7000/3
    elif request.endswith('.jpg'):
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open(myF+".jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())
        connectionSocket.close()

    elif request.endswith('.css'):
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open(myF + ".css", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())
        connectionSocket.close()


    elif request.endswith('SortByName'):
        import pandas as pd

        df = pd.read_csv("list.csv")# read the unsorted data
        sorted_df = df.sort_values(by=["name"], ascending=True)# sort the data by ascending order by names
        # to save data in a file after sorting
        sorted_df.to_csv('nameSort.csv', index=False)# put the sorted data in nameSort.csv file

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        my_file = open("nameSort.csv", "r")# read the file with sorted data
        content_list = my_file.readlines()# read line by line
        html = " <html><head><title> sorted Name </title> <body> <h1><br><font color=\"Navy\"> Smart phone sorted name <br>  <font color=\"blue\"> </h1> <h3><ol> <li>  " + content_list.__getitem__(
            0) + "    <li>" + content_list.__getitem__(1) + " " \
                                                            "   <li> " + content_list.__getitem__(
            2) + "   <li>  " + content_list.__getitem__(3) + "   <li> " + content_list.__getitem__(
            4) + "   <li> " + content_list.__getitem__(5) + " <li> " \
               + content_list.__getitem__(6) + "  <li> " + content_list.__getitem__(
            7) + "  <li> " + content_list.__getitem__(8) + "  <li> " + content_list.__getitem__(9) + "   <li> " + content_list.__getitem__(
            10) +  "  </ol>  </h3>"# print the list
        connectionSocket.send(html.encode())


    elif request.endswith('SortByPrice'):
        import pandas as pd

        df = pd.read_csv("list.csv")
        sorted_df = df.sort_values(by=["price"], ascending=True)
        # to save data in a file after sorting
        sorted_df.to_csv('priceSort.csv', index=False)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())

        my_file = open("priceSort.csv", "r")
        content_list = my_file.readlines()
        html = " <html><head><title> sorted Price </title> <body> <h1><br><font color=\"Burgundy\"> Smart phone sorted Price <br>  <font color=\"black\"> </h1> <h3><ol> <li> " + content_list.__getitem__(
            0) + "" \
                 "    <li>" + content_list.__getitem__(1) + "  <li> " + content_list.__getitem__(
            2) + "   <li>  " + content_list.__getitem__(3) + "   <li> " + content_list.__getitem__(4) + "" \
                                                                                                        "   <li> " + content_list.__getitem__(
            5) + " <li> " + content_list.__getitem__(6) + "  <li> " + content_list.__getitem__(
            7) + "  <li> " + content_list.__getitem__(8) + " " \
                                                           " <li> " + content_list.__getitem__(9) + "  </ol>  </h3>"
        connectionSocket.send(html.encode())

    else:# if the request didn't end with any of the previous option display an error
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=ISO-8859-1\r\n\r\n".encode())

        s = "<html><head><title > ERROR </title > </head><body>  <h1><br><font color=\"red\"> The file is not found <br> <font color=\"black\"> </h1><p><b>Siham Abu Remaileh 1180548</p><p><b>Sondos Nazzal 1180326</p> <p><b>Entimaa Rummaneh 1180841</p><h2> IP=" + str(  ip) + "port=" + str(port) + "</h2></body></html>\r\n"
        connectionSocket.send(s.encode())
        connectionSocket.close()



