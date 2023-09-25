import conllu

def count_di_and_ki_sconj(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counters for 'di' and 'ki' as SCONJ
    di_sconj_count = 0
    ki_sconj_count = 0
    total_sconj_count = 0
    di_sconj_examples = []
    ki_sconj_examples = []

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["lemma"] == "di" and token["upostag"] == "SCONJ":
                di_sconj_count += 1
                total_sconj_count += 1
                # Store example: (word, sentence_id)
                di_sconj_examples.append((token["form"], sentence.metadata["sent_id"]))
            elif token["lemma"] == "ki" and token["upostag"] == "SCONJ":
                ki_sconj_count += 1
                total_sconj_count += 1
                # Store example: (word, sentence_id)
                ki_sconj_examples.append((token["form"], sentence.metadata["sent_id"]))
            elif token["upostag"] == "SCONJ":
                total_sconj_count += 1

    # Calculate the percentage for 'di' and 'ki' as SCONJ
    if total_sconj_count > 0:
        percentage_di_sconj = (di_sconj_count / total_sconj_count) * 100
        percentage_ki_sconj = (ki_sconj_count / total_sconj_count) * 100
    else:
        percentage_di_sconj = 0
        percentage_ki_sconj = 0

    return di_sconj_count, ki_sconj_count, total_sconj_count, percentage_di_sconj, percentage_ki_sconj, di_sconj_examples, ki_sconj_examples

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    di_sconj_count, ki_sconj_count, total_sconj_count, percentage_di_sconj, percentage_ki_sconj, di_sconj_examples, ki_sconj_examples = count_di_and_ki_sconj(conllu_file)

    print("Occurrences of 'di' as SCONJ:", di_sconj_count)
    print("Occurrences of 'ki' as SCONJ:", ki_sconj_count)
    print("Total occurrences of SCONJ:", total_sconj_count)
    print("Percentage of 'di' as SCONJ: {:.2f}%".format(percentage_di_sconj))
    print("Percentage of 'ki' as SCONJ: {:.2f}%".format(percentage_ki_sconj))

    # Print examples for 'di' as SCONJ
    print("\nExamples of 'di' as SCONJ:")
    for example in di_sconj_examples:
        print("Word: {}, Sentence ID: {}".format(example[0], example[1]))

    # Print examples for 'ki' as SCONJ
    print("\nExamples of 'ki' as SCONJ:")
    for example in ki_sconj_examples:
        print("Word: {}, Sentence ID: {}".format(example[0], example[1]))
