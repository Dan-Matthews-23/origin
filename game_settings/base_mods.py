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


def diplomatic_timeline_events(request):
    events = {
        "Propose Non-Aggression Pact": {
            "user_event": "You proposed a Non-Aggression Pact",
            "target_event": "They proposed a Non-Aggression Pact",
        },

        "Accept Non-Aggression Pact Proposal": {
            "user_event": "You accepted a Non-Aggression Pact proposal",
            "target_event": "They accepted a Non-Aggression Pact proposal",
        },

        "Reject Non-Aggression Pact Proposal": {
            "user_event": "You rejected a Non-Aggression Pact proposal",
            "target_event": "They rejected a Non-Aggression Pact proposal",
        },

        "Propose Alliance": {
            "user_event": "You proposed an alliance",
            "target_event": "They proposed an alliance",
        },

        "Accept Alliance Proposal": {
            "user_event": "You accepted an alliance proposal",
            "target_event": "They accepted an alliance proposal",
        },

         "Reject Alliance Proposal": {
            "user_event": "You rejected an alliance proposal",
            "target_event": "They rejected an alliance proposal",
        },

        "Declare War": {
            "user_event": "You declared war",
            "target_event": "They declared war",
        },

        "End Alliance": {
            "user_event": "You ended your alliance",
            "target_event": "They ended your alliance",
        },

        "Non-Aggression Pact Expired": {
            "user_event": "Your Non-Aggression Pact expired",
            "target_event": "Your Non-Aggression Pact expired",
        },

        "Set relations to Neutral": {
            "user_event": "You set your relations to neutral",
            "target_event": "They set your relations to neutral",
        }        
    }
    return events



