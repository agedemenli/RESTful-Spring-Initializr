import os

from javaconverterstyler import get_java_type, to_class_name, to_camelcase


def create_controllers(java_coder, entities, app_name):
    # Create directory
    path = app_name + "/src/main/java/com/" + app_name + "/" + app_name + "app/controller"
    os.system("mkdir " + path)
    bline = java_coder.get_beautify_line()
    bspace = java_coder.get_beautify_space()
    indent = java_coder.get_indentation()
    for entity in entities:
        # Create class
        entity_name = entity.get("entity_name")
        class_name = to_class_name(entity_name)
        service_variable = entity_name + "Service"
        service_class = class_name + "Service"
        file = open(path + "/" + class_name + "Controller.java", "w+")
        file.write("import org.springframework.web.bind.annotation.*;\n")
        file.write("import com." + app_name + "." + app_name + "app.service." + service_class + ";\n")
        file.write(bline + "@RestController\n")
        file.write("public class " + class_name + "Controller" + java_coder.open_scope(1))
        file.write(bline + indent + "private final " + service_class + " " + service_variable + ";\n")
        # Constructor
        file.write(bline + indent + "public " + class_name + "Controller(" + service_class + " ")
        file.write(service_variable + ")" + java_coder.open_scope(1))
        file.write(indent * 2 + "this." + service_variable + bspace + "=" + bspace + service_variable + ";\n")
        file.write(indent + "}\n")
        # CRUD by id
        # Get by id
        file.write(bline + indent + "@GetMapping\n")
        file.write(indent + "public " + class_name + " get" + class_name + "ById(@RequestParam Long id)")
        file.write(java_coder.open_scope(2))
        file.write(indent * 2 + "return " + entity_name + "Service.get" + class_name + "ById(id);\n")
        file.write(indent + "}\n")
        file.write("}")
