def format_currency(amount):
    return "${:,.2f}".format(amount)

def validate_input(input_value, input_type):
    if input_type == 'int':
        return isinstance(input_value, int) and input_value >= 0
    elif input_type == 'float':
        return isinstance(input_value, float) and input_value >= 0.0
    elif input_type == 'str':
        return isinstance(input_value, str) and len(input_value) > 0
    return False
