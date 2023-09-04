from django import template

register = template.Library()

@register.filter
def format_time(hour, minute):
    return f"{hour:02d}:{minute:02d}"

@register.filter
def get_range(value, args=''):
    if args == '':
        start, end, step = value, 1
    elif type(args) == int:
        start, end, step = value, args, 1
    else:
        start, end, step = value, *map(int, args.split(':'))
    if not step:
        step = 1
    return range(start, end, step)
