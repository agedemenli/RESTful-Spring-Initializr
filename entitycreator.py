import os

from javaconverterstyler import get_java_type, to_class_name, to_camelcase


def create_entities(java_coder, entities, app_name):
    # Create directory
    path = app_name + "/src/main/java/com/" + app_name + "/" + app_name + "app/entity"
    os.system("mkdir " + path)
    bline = java_coder.get_beautify_line()
    bspace = java_coder.get_beautify_space()
    indent = java_coder.get_indentation()
    for entity in entities:
        # Create class
        entity_name = entity.get("entity_name")
        class_name = to_class_name(entity_name)
        file = open(path + "/" + class_name + ".java", "w+")
        file.write("public class " + class_name + java_coder.open_scope(1))
        fields = entity.get("fields")
        # Add fields
        for field in fields:
            file.write(bline + indent + "private " + get_java_type(field.get("type")) + " " +
                       to_camelcase(field.get("field_name")) + ";\n")
        # Add getters & setters
        for field in fields:
            field_name = to_camelcase(field.get("field_name"))
            field_name_capitalized = to_class_name(field.get("field_name"))
            field_type = get_java_type(field.get("type"))
            open_scope = java_coder.open_scope(1)
            # Add getter
            file.write(bline + indent + "public " + field_type + " get" + field_name_capitalized + "()")
            file.write(open_scope)
            file.write(indent * 2 + "return this." + field_name + ";\n")
            file.write(indent + "}\n")
            # Add setter
            file.write(bline + indent + "public void set" + field_name_capitalized)
            file.write("(" + field_type + " " + field_name + ")")
            file.write(open_scope)
            file.write(indent * 2 + "this." + field_name + bspace + "=" + bspace + field_name + ";\n")
            file.write(indent + "}\n")
        file.write("}")
