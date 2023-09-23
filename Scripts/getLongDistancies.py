import conllu

def analyze_conllu_file(conllu_file_path, max_distance):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counts
    long_distance_dependencies = 0

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "nsubj" or token["deprel"] == "obj":
                # Calculate the distance between the dependent and its head
                distance = abs(token["id"] - token["head"])
                if distance > max_distance:
                    long_distance_dependencies += 1

    print(f"Long-distance dependencies (beyond {max_distance} tokens): {long_distance_dependencies}")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    max_distance = 5  # Adjust the maximum distance as needed
    analyze_conllu_file(conllu_file, max_distance)

