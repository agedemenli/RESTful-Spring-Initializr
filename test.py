import os

os.system('curl https://start.spring.io/starter.zip -o demo.zip')
os.system('unzip demo.zip -d demo')
os.system('mkdir demo/src/main/java/com/example/demo/controller')
applicationJava = open("demo/src/main/java/com/example/demo/controller/UserController.java", "w+")
indent = '  '
space = ' '
applicationJava.write(indent * 0 + 'public class UserController' + space + '{\n')
applicationJava.write(indent * 1 + 'public static void Main()' + space + '{\n')
applicationJava.write(indent * 2 + 'return;\n')
applicationJava.write(indent * 1 + '}\n')
applicationJava.write(indent * 0 + '}\n')
# test line
