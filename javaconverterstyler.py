class JavaConverterStyler:

    def __init__(self, indentation_space_count, open_curly_brackets_same_line, beautify_with_spaces,
                 beautify_with_blank_lines):
        self.indentation_space_count = indentation_space_count if indentation_space_count else 2
        self.open_curly_brackets_same_line = open_curly_brackets_same_line if open_curly_brackets_same_line else True
        self.beautify_with_spaces = beautify_with_spaces if beautify_with_spaces else True
        self.beautify_with_blank_lines = beautify_with_blank_lines if beautify_with_blank_lines else True

    def get_indentation(self):
        return self.indentation_space_count * ' '

    def get_char_before_curly(self):
        return ' ' if self.open_curly_brackets_same_line else '\n'

    def get_beautify_space(self):
        return ' ' if self.beautify_with_spaces else ''

    def get_beautify_line(self):
        return '\n' if self.beautify_with_blank_lines else ''


def get_java_type(db_type):
    java_types = {
        "varchar": "String",
        "integer": "Integer",
        "bigint": "Long",
        "boolean": "Boolean"
    }
    db_type = db_type[0:7]
    java_type = java_types.get(db_type)
    if java_type:
        return java_type
    else:
        raise Exception


def to_camelcase(value):
    first, *rest = value.split('_')
    return first + ''.join(word.capitalize() for word in rest)


def to_class_name(value):
    camelcase = to_camelcase(value)
    return camelcase[0].capitalize() + camelcase[1:]
