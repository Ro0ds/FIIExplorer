def remove_html_tags(text, str_to_remove):
    text_string_removed = text.replace(str_to_remove, '')

    while True:
        if str(text_string_removed).startswith('<>') or str(text_string_removed).endswith('</>'):
            text_string_removed = text.replace(str_to_remove, '')
            text_string_removed = text_string_removed.replace('<>', '')
            text_string_removed = text_string_removed.replace('</>', '')
        else:
            break

    return text_string_removed
