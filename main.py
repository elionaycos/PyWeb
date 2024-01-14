from source.helper.server import Server

class PyWeb:
    def __init__(self):
        self.server = Server("127.0.0.1",1080)
        self.server.create()
        html_raw = open("source/html/index.html")
        html = html_raw.read()
        while True:
            self.server.send(html)






if __name__ == "__main__":
    try:
        PyWeb()
    except Exception as error:
        print(f"Error Na função principal: {str(error)}")