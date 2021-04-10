import cherrypy
from app import Root

app = cherrypy.tree.mount(Root(), '/')

if __name__=='__main__':

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 9000,
        'server.max_request_body_size' : 157286400,
    })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.quickstart(Root())