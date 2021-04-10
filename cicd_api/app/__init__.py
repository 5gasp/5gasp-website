import cherrypy
import os
from datetime import datetime

class Root(object):
    # key
    key= 'pE9VbS@JWGyK:,K:'
    git_repo_path = 'xxx'
    # jekyll
    site_output_base_path = '/Users/rd/Desktop/UA/UA_9_Semestre/5GASP/Website/cicd_api'
    site_output_zip_name = 'website.zip'
    site_output_dir_name = 'website'
    # nginx
    nginx_source_dir = 'xxx'
    served_dir_name = 'xxx'
    backup_dir_name = 'xxx-old'
    timestamp_file = 'xxx'


    post_commands = [
            (f"rm -rf {os.path.join(site_output_base_path, site_output_dir_name)} ", "Couldn't remove the genereated website dir."),
            (f"unzip {os.path.join(site_output_base_path, site_output_zip_name)} -d {os.path.join(site_output_base_path, site_output_dir_name)}", "Couldn't unzip website to nginx dir."),
            (f"rm -rf {os.path.join(nginx_source_dir, site_output_dir_name)} && mv {os.path.join(site_output_base_path, site_output_dir_name)} {nginx_source_dir}", "Couldn't move the output website to nginx dir."),
            (f"cd {nginx_source_dir} && rm -rf {backup_dir_name} && mv {served_dir_name} {backup_dir_name}", "Couldn't generate backup of the last version."),
            (f"cd {nginx_source_dir} && mv {site_output_dir_name} {served_dir_name}", "Couldn't update the directory that is being served."),
            (f"echo $(date) > {os.path.join(nginx_source_dir, served_dir_name, timestamp_file)}", "Couldn't update the timestamp.")
    ]

    @cherrypy.expose
    def index(self, key=None, website_zip=None):
        print(cherrypy.request.method)
        cherrypy.request.show_tracebacks = False
        if  cherrypy.request.method == 'POST':
            print("POST")
            # get key
            if not key:
                return "No key received"

            if key != self.key:
                return "The key is incorrect"


            # read file content
            try:
                whole_data = bytearray()
                while True:
                    data = website_zip.file.read(8192)
                    whole_data += data # Save data chunks in ByteArray whole_data

                    if not data:
                        break

                written_file = open(os.path.join(self.site_output_base_path, self.site_output_zip_name), "wb") # open file in write bytes mode
                written_file.write(whole_data) # write file
            except Exception as e:
                print(e)
                return "Couldn't read the uploaded file"

            # deploy in nginx
            for command, error in self.post_commands:
                if os.system(command) != 0:
                    return error

            return "Updated"

        elif cherrypy.request.method == 'GET':
            print("GET")
            try:
                f = open(os.path.join(self.nginx_source_dir, self.served_dir_name, self.timestamp_file))
                update = f.readline()
                return "Last Update: " + update
            except:
                return "Error getting the last update timestamp"


        else:
            return "Not allowed!"