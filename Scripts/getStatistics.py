from collections import defaultdict

def analyze_conllu_file(conllu_file):
    # Create dictionaries to store information about UPOS tags, word types, and lemmas
    upos_tags = set()
    word_types = defaultdict(set)
    lemmas = defaultdict(set)
    auxiliary_count = 0
    marker_count = 0
    total_count = 0  # Initialize the total count

    with open(conllu_file, 'r', encoding='utf-8') as f:
        # Split the file into sentences
        sentences = f.read().strip().split('\n\n')

    for sentence in sentences:
        lines = sentence.split('\n')

        # Process each line in the sentence
        for line in lines:
            # Skip comments and empty lines
            if line.startswith('#') or line.strip() == '':
                continue

            # Split the line into fields
            fields = line.strip().split('\t')

            # Ensure that the line has the expected number of fields (10 in CoNLL-U format)
            if len(fields) != 10:
                continue

            # Extract the UPOS tag (the 4th field)
            upos = fields[3]

            # Extract the word form (the 2nd field)
            word_form = fields[1]

            # Extract the lemma (the 2nd field)
            lemma = fields[2]

            upos_tags.add(upos)

            if upos == "PART":
                word_types[word_form].add(lemma)

            if upos == "PRON" or upos == "DET":
                lemmas[word_form].add(lemma)

            # Check if the word is "να"
            if word_form == "να":
                total_count += 1  # Increment the total count

                # Extract the dependency relationship (the 7th field)
                deprel = fields[7]

                # Check if "να" is an auxiliary
                if upos == "AUX":
                    auxiliary_count += 1

                # Check if "να" is a marker
                if deprel == "mark":
                    marker_count += 1

    # Calculate lemmas that occurred as both PRON and DET
    shared_lemmas = set(lemmas.keys()) & set(word_types.keys())

    # Print the statistics
    # Calculate percentages
    auxiliary_percentage = (auxiliary_count / total_count) * 100 if total_count > 0 else 0
    marker_percentage = (marker_count / total_count) * 100 if total_count > 0 else 0

    # Print the counts and percentages
    print(f"Count of 'να' as an auxiliary: {auxiliary_count} ({auxiliary_percentage:.2f}%)")
    print(f"Count of 'να' as a marker: {marker_count} ({marker_percentage:.2f}%)")

    print(f"This corpus uses {len(upos_tags)} UPOS tags out of 17 possible: {', '.join(upos_tags)}")
    print(f"This corpus does not use the following tags: {', '.join(set(['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']) - upos_tags)}")
    print(f"This corpus contains {len(word_types)} word types tagged as particles (PART): {', '.join(word_types.keys())}")
    print(f"This corpus contains {len(lemmas)} lemmas tagged as pronouns (PRON) or determiners (DET):")
    for word, lemma_set in lemmas.items():
        print(f"{word} ({', '.join(lemma_set)})")
    print(f"Out of the above, {len(shared_lemmas)} lemmas occurred sometimes as PRON and sometimes as DET: {', '.join(shared_lemmas)}")

if __name__ == "__main__":
    conllu_file = "C:\\Users\iness\\Desktop\\LRL\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
