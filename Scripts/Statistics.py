from collections import defaultdict

def analyze_conllu_file(conllu_file):
    # Create dictionaries to store information about root relations and other specified features
    root_as_verb_count = 0
    root_as_other_count = 0
    cconj_count = 0
    apposition_count = 0
    mediator_count = 0
    right_subject_count = 0
    dependent_subject_count = 0
    left_object_count = 0

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

            # Extract the dependency relationship (the 7th field)
            deprel = fields[7]

            # Check if the word is a root
            if deprel == 'root':
                if upos == 'VERB':
                    root_as_verb_count += 1
                else:
                    root_as_other_count += 1

            # Check for other specified features
            if deprel == 'cconj':
                cconj_count += 1

            if deprel == 'appos':
                apposition_count += 1

            if upos in ['ADP', 'SCONJ']:
                mediator_count += 1

            if deprel == 'nsubj':
                if fields[6] != '0':
                    dependent_subject_count += 1
                else:
                    right_subject_count += 1

            if deprel == 'obj' and upos != 'PRON':
                left_object_count += 1

    total_sentences = len(sentences)

    # Calculate percentages
    root_as_verb_percentage = (root_as_verb_count / total_sentences) * 100
    root_as_other_percentage = (root_as_other_count / total_sentences) * 100
    cconj_percentage = (cconj_count / total_sentences) * 100
    apposition_percentage = (apposition_count / total_sentences) * 100
    mediator_percentage = (mediator_count / total_sentences) * 100
    right_subject_percentage = (right_subject_count / total_sentences) * 100
    dependent_subject_percentage = (dependent_subject_count / total_sentences) * 100
    left_object_percentage = (left_object_count / total_sentences) * 100

    # Print the results
    print(f"Percentage of root as VERB: {root_as_verb_percentage:.2f}%")
    print(f"Percentage of root as OTHER: {root_as_other_percentage:.2f}%")
    print(f"Percentage of cconj dependency: {cconj_percentage:.2f}%")
    print(f"Percentage of appos dependency: {apposition_percentage:.2f}%")
    print(f"Percentage of mediator (ADP or SCONJ): {mediator_percentage:.2f}%")
    print(f"Percentage of right subjects: {right_subject_percentage:.2f}%")
    print(f"Percentage of dependent subjects: {dependent_subject_percentage:.2f}%")
    print(f"Percentage of left objects (non-pronominal): {left_object_percentage:.2f}%")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
