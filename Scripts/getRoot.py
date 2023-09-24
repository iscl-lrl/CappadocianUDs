import conllu

def analyze_conllu_file(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counts
    total_roots = 0
    verb_roots = 0
    other_roots = 0
    total_verbs = 0

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "root":
                total_roots += 1
                if token["upostag"] == "VERB":
                    verb_roots += 1
                else:
                    other_roots += 1
            if token["upostag"] == "VERB":
                total_verbs += 1

    # Calculate percentages
    if total_roots > 0:
        percentage_verb_roots = (verb_roots / total_roots) * 100
        percentage_other_roots = (other_roots / total_roots) * 100
    else:
        percentage_verb_roots = 0
        percentage_other_roots = 0

    print(f"Total roots: {total_roots}")
    print(f"Roots as verbs: {verb_roots} ({percentage_verb_roots:.2f}%)")
    print(f"Roots as other parts of speech: {other_roots} ({percentage_other_roots:.2f}%)")
    print(f"Total verbs: {total_verbs}")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
