import os


class Initializr:
    def __init__(self, input_params):
        self.app_name = input_params['app_name']
        # self.make_curl()
        # self.unzip()

    def make_curl(self):
        os.system('curl https://start.spring.io/starter.zip -d dependencies=security,web -d name=' + self.app_name +
                  ' -d language=java -d type=maven-project -d artifactId=' + self.app_name +
                  'app -d groupId=com.' + self.app_name + ' -o ' + self.app_name + '_initial.zip')

    def unzip(self):
        os.system('unzip ' + self.app_name + '_initial.zip -d ' + self.app_name)
