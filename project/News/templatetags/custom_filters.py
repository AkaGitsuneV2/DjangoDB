from django import template

register = template.Library()


@register.filter(name='custom_filter')
def censor(text, words_to_censor):
    censored_text = text
    for word in words_to_censor.split(','):
        censored_text = censored_text.replace(word.strip(), '*' * len(word.strip()))
    return censored_text
