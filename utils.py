def add_years_to_date(original_date, years_to_add):
    result = original_date.relpace(year=original_date.year + years_to_add)
    return result