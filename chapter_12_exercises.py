#CHAPTER 12 EXERCISES

#Exercise 1

def ex1():

    import socket

    try:
        siteName = input('Enter the site you want to call:')

        x = siteName.split('/')
        print(x)
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((x[2], 80))
        urlString = 'GET ' + str(siteName) + ' HTTP/1.0\r\n\r\n'
        print('Debug: ', urlString)
        cmd = urlString.encode()
        print(cmd)
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')

        mysock.close()
    
    except:
        print('The site cannot be accessed as entered')


#ex1()


def ex1PlusURLLib():

    import socket
    import urllib.parse


    siteQuery = input('Enter the site you want to call:')
    urlParsing = urllib.parse.urlparse(siteQuery)


    print(urlParsing)
    print(urlParsing.hostname)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((urlParsing.hostname, 80))
    urlString = 'GET ' + siteQuery + ' HTTP/1.0\r\n\r\n'
    print('Debug: ', urlString)
    cmd = urlString.encode()
    print(cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
    

#ex1PlusURLLib()

#Exercise 2
def ex2():

    import socket

    
    siteName = input('Enter the site you want to call:')

    x = siteName.split('/')
    print(x)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((x[2], 80))
    urlString = 'GET ' + str(siteName) + ' HTTP/1.0\r\n\r\n'
    print('Debug: ', urlString)
    cmd = urlString.encode()
    print(cmd)
    mysock.send(cmd)


    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        countData = data.decode()
        print('Debug count: ', countData)
        #sliceSize = slice(2999)
        scrData = countData[:2999]



        print(scrData, len(countData), end='')

    mysock.close()
    

ex2()