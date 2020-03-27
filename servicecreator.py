import os

from javaconverterstyler import get_java_type, to_class_name, to_camelcase


def create_services(java_coder, entities, app_name):
    # Create directory
    path = app_name + "/src/main/java/com/" + app_name + "/" + app_name + "app/service"
    os.system("mkdir " + path)
    bline = java_coder.get_beautify_line()
    bspace = java_coder.get_beautify_space()
    indent = java_coder.get_indentation()
    for entity in entities:
        # Create class
        entity_name = entity.get("entity_name")
        class_name = to_class_name(entity_name)
        repository_variable = entity_name + "Repository"
        repository_class = class_name + "Repository"
        file = open(path + "/" + class_name + "Service.java", "w+")
        file.write("import org.springframework.web.bind.annotation.*;\n")
        file.write("import com." + app_name + "." + app_name + "app.repository." + repository_class + ";\n")
        file.write(bline + "@Service\n")
        file.write("public class " + class_name + "Service" + java_coder.open_scope(1))
        file.write(bline + indent + "private final " + repository_class + " " + repository_variable + ";\n")
        # Constructor
        file.write(bline + indent + "public " + class_name + "Service(" + repository_class + " ")
        file.write(repository_variable + ")" + java_coder.open_scope(1))
        file.write(indent * 2 + "this." + repository_variable + bspace + "=" + bspace + repository_variable + ";\n")
        file.write(indent + "}\n")
        # CRUD by id
        # Get by id
        file.write(bline + indent + "public " + class_name + " get" + class_name + "ById(Long id)")
        file.write(java_coder.open_scope(2))
        file.write(indent * 2 + "return " + entity_name + "Repository.get" + class_name + "ById(id);\n")
        file.write(indent + "}\n")
        file.write("}")
