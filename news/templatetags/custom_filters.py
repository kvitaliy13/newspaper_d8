from django import template


register = template.Library()

words =['рассказал','Укрэнерго', 'мир']


@register.filter()
def censor(value):
    for word in words:
        value = value.replace(word, word[0] + '*' * len(word))
    return value



