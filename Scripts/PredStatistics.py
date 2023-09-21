def analyze_conllu_file(conllu_file):
    with open(conllu_file, 'r', encoding='utf-8') as f:
        # Split the file into sentences
        sentences = f.read().strip().split('\n\n')

    total_words = 0
    head_dict = {}
    relation_dict = {}

    # Process each sentence
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

            # Extract word, head, and dependency relation
            word = fields[1]
            head = int(fields[6])  # The 7th field (index 6) contains the head information
            deprel = fields[7]

            # Store head and relation in dictionaries
            head_dict[word] = head
            relation_dict[word] = deprel
            total_words += 1

    # Initialize counters for head and relation frequencies
    head_counts = {}
    relation_counts = {}

    # Count the occurrences of each head and relation
    for word, head in head_dict.items():
        relation = relation_dict.get(word, 'None')  # Get the relation or 'None' if not found

        if head not in head_counts:
            head_counts[head] = 0
        head_counts[head] += 1

        if relation not in relation_counts:
            relation_counts[relation] = 0
        relation_counts[relation] += 1

    # Calculate and print the percentages
    print("Heads:")
    for head, count in head_counts.items():
        percentage = (count / total_words) * 100
        print(f"Head {head}: {percentage:.2f}%")

    print("\nRelations:")
    for relation, count in relation_counts.items():
        percentage = (count / total_words) * 100
        print(f"Relation {relation}: {percentage:.2f}%")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
