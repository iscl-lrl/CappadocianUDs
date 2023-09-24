import conllu

def analyze_conllu_file(conllu_file_path, max_distance):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counts and a list for examples
    long_distance_dependencies = 0
    long_distance_examples = []

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "nsubj" or token["deprel"] == "obj":
                # Calculate the distance between the dependent and its head
                distance = abs(token["id"] - token["head"])
                if distance > max_distance:
                    long_distance_dependencies += 1
                    # Store the example
                    example = {
                        "form": token["form"],
                        "deprel": token["deprel"],
                        "head_form": sentence[token["head"] - 1]["form"],  # Get the head's form
                        "distance": distance
                    }
                    long_distance_examples.append(example)

    print(f"Long-distance dependencies (beyond {max_distance} tokens): {long_distance_dependencies}")

    # Print examples
    if long_distance_examples:
        print("\nExamples of long-distance dependencies:")
        for example in long_distance_examples:
            print(f"Form: {example['form']}, Deprel: {example['deprel']}, Head Form: {example['head_form']}, Distance: {example['distance']}")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    max_distance = 5  # Adjust the maximum distance as needed
    analyze_conllu_file(conllu_file, max_distance)
