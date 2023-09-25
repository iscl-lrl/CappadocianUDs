import conllu

def count_nmod_left_of_parent(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counters
    nmod_left_count = 0
    total_nmod_count = 0
    nmod_examples = []

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "nmod":
                total_nmod_count += 1
                if token["head"] > token["id"]:
                    nmod_left_count += 1
                    # Store example: (word, parent_word, sentence_id)
                    parent_token = sentence[token["head"] - 1]
                    nmod_examples.append((token["form"], parent_token["form"], sentence.metadata["sent_id"]))

    # Calculate the percentage
    if total_nmod_count > 0:
        percentage_nmod_left = (nmod_left_count / total_nmod_count) * 100
    else:
        percentage_nmod_left = 0

    return nmod_left_count, total_nmod_count, percentage_nmod_left, nmod_examples

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    nmod_left, total_nmod, percentage_nmod_left, nmod_examples = count_nmod_left_of_parent(conllu_file)

    print("Occurrences of nmod to the left of their parent:", nmod_left)
    print("Total occurrences of nmod:", total_nmod)
    print("Percentage of nmod to the left: {:.2f}%".format(percentage_nmod_left))

    # Print examples
    print("\nExamples of nmod to the left of their parent:")
    for example in nmod_examples:
        print("Word: {}, Parent Word: {}, Sentence ID: {}".format(example[0], example[1], example[2]))
