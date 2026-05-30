def calculate_urgency(text):
    text = text.lower()

    score = 1

    keywords = {
        "domani": 10,
        "oggi": 10,
        "subito": 10,
        "urgentissimo": 10,
        "urgente": 8,
        "scadenza": 8,
        "entro": 6,
        "settimana": 5,
        "mese": 3
    }

    for word, value in keywords.items():
        if word in text:
            score = max(score, value)

    return score
    
def calculate_importance(text):
    text = text.lower()

    score = 1

    keywords = {
    	"macchina": 10,
    	"automobile": 10,
        "tesi": 9,
        "esame": 8,
        "università": 8,
        "lavoro": 8,
        "progetto": 7,
        "studio": 6,
        "libro": 5,
        "pc": 8,
        "computer": 8,
        "telefono": 6,
        "hobby": 1,
        "gioco": 1
    }

    for word, value in keywords.items():
        if word in text:
            score = max(score, value)

    return score

def request_priority(text, time):
	return calculate_urgency(text) + calculate_importance(text) - time

def offer_priority(itemName, requests):
    count = 0

    for request in requests:
        if request.itemName == itemName:
            count += 1

    return count