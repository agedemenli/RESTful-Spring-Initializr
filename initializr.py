import os


class Initializr:
    def __init__(self, initializr_params):
        self.app_name = initializr_params['app_name']
        os.system("rm -rf " + self.app_name + "*")

    def make_curl(self):
        os.system('curl https://start.spring.io/starter.zip -d dependencies=security,web -d name=' + self.app_name +
                  ' -d language=java -d type=maven-project -d artifactId=' + self.app_name +
                  'app -d groupId=com.' + self.app_name + ' -o ' + self.app_name + '_initial.zip')

    def unzip(self):
        os.system('unzip ' + self.app_name + '_initial.zip -d ' + self.app_name)


def initialize_project(user_inp):
    # Create template using start.spring.io
    initializr_keys = ['app_name']  # todo: add more
    initializr_parameters = {x: user_inp[x] for x in initializr_keys}
    init = Initializr(initializr_parameters)
    init.make_curl()
    init.unzip()
