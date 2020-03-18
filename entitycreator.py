import os

from javaconverterstyler import get_java_type, to_class_name, to_camelcase


def create_entities(java_coder, entities, app_name):
    path = app_name + "/src/main/java/com/" + app_name + "/" + app_name + "app/entity"
    os.system("mkdir " + path)
    bline = java_coder.get_beautify_line()
    bcurly = java_coder.get_char_before_curly()
    indent = java_coder.get_indentation()
    for entity in entities:
        entity_name = entity.get("entity_name")
        class_name = to_class_name(entity_name)
        file = open(path + "/" + class_name + ".java", "w+")
        file.write("public class " + class_name + bcurly + "{\n")
        fields = entity.get("fields")
        for field in fields:
            file.write(bline + indent + "private " + get_java_type(field.get("type")) + " " +
                       to_camelcase(field.get("field_name")) + ";\n")
        file.write("}")
