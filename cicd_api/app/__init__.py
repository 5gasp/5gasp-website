import cherrypy
import os
from datetime import datetime

class Root(object):
    # key
    key= 'xxx'
    git_repo_path = 'xxx'
    # jekyll
    site_output_base_path = 'xxx'
    site_output_dir_name = 'xxx'
    # nginx
    nginx_source_dir = 'xxx'
    served_dir_name = 'xxx'
    backup_dir_name = 'xxx-old'
    timestamp_file = 'xxx'


    post_commands = [
        (f"cd {git_repo_path} && git pull", "Couldn't pull the repository."),
        (f"cd {git_repo_path} && jekyll build -d {os.path.join(site_output_base_path, site_output_dir_name)}", "Couldn't build the jekyll project."),
        (f"rm -rf {os.path.join(nginx_source_dir, site_output_dir_name)} && mv {os.path.join(site_output_base_path, site_output_dir_name)} {nginx_source_dir}", "Couldn't move the output website to nginx dir."),
        (f"cd {nginx_source_dir} && rm -rf {backup_dir_name} && mv {served_dir_name} {backup_dir_name}", "Couldn't generate backup of the last version."),
        (f"cd {nginx_source_dir} && mv {site_output_dir_name} {served_dir_name}", "Couldn't update the directory that is being served."),
        (f"echo {str(datetime.now())} > {os.path.join(nginx_source_dir, served_dir_name, timestamp_file)}", "Couldn't update the timestamp.")
    ]   

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def index(self):
        cherrypy.request.show_tracebacks = False
        if  cherrypy.request.method == 'POST':
            # get key
            try:
                input_json = cherrypy.request.json
                key = input_json["key"]
            except:
                return "No key received"

            if key != self.key:
                return "The key is incorrect"

            # run all commands
            for command, error in self.post_commands:
                if os.system(command) != 0:
                    return error
            return "Updated"
        
        elif cherrypy.request.method == 'GET':
                try:    
                f = open(os.path.join(self.nginx_source_dir, self.served_dir_name, self.timestamp_file))
                update = f.readline()
                return "Last Update: " + update
            except:
                return "Error getting the last update timestamp"


        else:
            return "Not allowed!"