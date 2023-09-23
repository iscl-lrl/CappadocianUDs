import conllu

def check_conjunction_positions(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counters for first-position and mediator conjunctions
    sconj_first_position = 0
    cconj_first_position = 0
    mediator_conjunctions = 0

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["upostag"] == "SCONJ":
                if int(token["id"]) == 1:
                    sconj_first_position += 1
                else:
                    mediator_conjunctions += 1
            elif token["upostag"] == "CCONJ":
                if int(token["id"]) == 1:
                    cconj_first_position += 1
                else:
                    mediator_conjunctions += 1

    return sconj_first_position, cconj_first_position, mediator_conjunctions

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"  
    sconj_first, cconj_first, mediators = check_conjunction_positions(conllu_file)
    
    print("Subordinating Conjunctions (SCONJ) in first position:", sconj_first)
    print("Coordinating Conjunctions (CCONJ) in first position:", cconj_first)
    print("Conjunctions used as mediators:", mediators)
