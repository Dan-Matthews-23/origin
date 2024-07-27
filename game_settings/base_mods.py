def powers(request):
    powers = {
            "Amazons": {
                "Attack": 0,
                "Defence": 0,
                "Intel": 25,
                "Income": 0
            },
            "Spartans": {
                "Attack": 25,
                "Defence": 0,
                "Intel": 0,
                "Income": 0
            },
            "Atlantians": {
                "Attack": 0,
                "Defence": 25,
                "Intel": 0,
                "Income": 0
            },
            "Witches": {
                "Attack": 0,
                "Defence": 0,
                "Intel": 0,
                "Income": 25
            }
        }
    return powers