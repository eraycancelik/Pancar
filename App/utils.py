def is_numeric(value):
        try:
            float(value)  # Değeri float türüne dönüştürmeye çalış
            return True  # Başarılı olduysa, değer sayısal bir ifadeydi
        except ValueError:
            return False 
        
def is_valid(input_string):
    allowed_chars = set('0123456789. ')
    return all(char in allowed_chars for char in input_string)