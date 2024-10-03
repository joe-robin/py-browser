import socket
class URL:
    def request(self):
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )

        s.connect((self.host,80))

        request = "GET {} HTTP/1.0\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "\r\n"
        

    def __init__(self,url):
        # seperate the scheme from the url and check if it is "http"
        self.scheme, url = url.split("://", 1)
        assert self.scheme == "http" # throws error if false
        # seperate the path from the host  if there is no path then the path will be just /
        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" +  url

