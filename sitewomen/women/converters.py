class FourDigitYearConverter:
    regex = r'[0-9]{4}'
    def to_python(self, value: str) -> int:
        return int(value)
    
    def to_url(self, value: int) -> int:
        return "%04d" % value