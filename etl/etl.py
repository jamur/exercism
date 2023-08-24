def transform(legacy_data: dict) -> dict:
    return {letter.lower(): value
            for value, letters in legacy_data.items()
            for letter in letters}

