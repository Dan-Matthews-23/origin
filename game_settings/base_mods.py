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

def data_crystal_from_attack(request):
    gain = {
        "Overwhelming Victory": {
            "base_gain": 75,
            "is_enemy": 90
            },
        "Clear Victory": {
            "base_gain": 60,
            "is_enemy": 75
            },
         "Victory": {
            "base_gain": 45,
            "is_enemy": 60
            },       
    }
    return gain


def troop_loss(request):
    loss = {
        "Overwhelming Victory": {
            "loss": 0,            
            },
        "Clear Victory": {            
            "loss": 0.10
            },
         "Victory": {           
            "loss": 0.15
            },
        "Defeat": {
            "loss": 0.15
        },
        "Clear Defeat": {
            "loss": 0.20
        },
        "Overwhelming Defeat": {
            "loss": 0.35
        },
    }
    return loss