def generate_sql(entities, app_name):
    # Create directory
    path = app_name
    file = open(path + "/" + "create_db.sql", "w+")
    file.write("CREATE DATABASE " + app_name + "_db;\n")
    for entity in entities:
        # Create class
        entity_name = entity.get("entity_name")
        file.write("CREATE TABLE " + entity_name + " (\n")
        columns = entity.get("fields")
        for column in columns:
            column_name = column.get("field_name")
            data_type = column.get("type")
            file.write(column_name + " " + data_type + ",\n")
        file.write(");\n")
