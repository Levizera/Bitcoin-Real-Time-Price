def remove_special_char(old_string, to_remove):
    new_string = old_string
    for special_char in to_remove:
        new_string = new_string.replace(special_char, '')
    return new_string