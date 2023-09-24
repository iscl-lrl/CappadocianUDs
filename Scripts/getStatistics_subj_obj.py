import conllu

def analyze_conllu_file(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counts and lists for examples
    total_subjects = 0
    subjects_to_right = 0
    total_objects = 0
    objects_to_left = 0
    subject_examples = []
    object_examples = []

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "nsubj":
                total_subjects += 1
                if token["head"] < token["id"]:
                    subjects_to_right += 1
                    # Get the form of the parent token
                    head_token = sentence[token["head"] - 1]  # Note the -1 since token["head"] is 1-based
                    subject_examples.append((token["form"], head_token["form"], token["id"]))
            elif token["deprel"] == "obj":
                total_objects += 1
                if token["head"] > token["id"]:
                    objects_to_left += 1
                    # Get the form of the parent token
                    head_token = sentence[token["head"] - 1]  # Note the -1 since token["head"] is 1-based
                    object_examples.append((token["form"], head_token["form"], token["id"]))

    # Calculate the percentages
    if total_subjects > 0:
        percentage_subjects_to_right = (subjects_to_right / total_subjects) * 100
    else:
        percentage_subjects_to_right = 0

    if total_objects > 0:
        percentage_objects_to_left = (objects_to_left / total_objects) * 100
    else:
        percentage_objects_to_left = 0

    print(f"Total subjects: {total_subjects}")
    print(f"Subjects to the right of their parent: {subjects_to_right}")
    print(f"Percentage subjects to the right: {percentage_subjects_to_right:.2f}%")
    print(f"Total objects: {total_objects}")
    print(f"Objects to the left of their parent: {objects_to_left}")
    print(f"Percentage objects to the left: {percentage_objects_to_left:.2f}%")

    # Print examples
    if subject_examples:
        print("\nExamples of nsubjects to the right of their parent:")
        for form, head_form, id in subject_examples:
            print(f"ID: {id}, Form: {form}, Parent Form: {head_form}")
    
    if object_examples:
        print("\nExamples of objects to the left of their parent:")
        for form, head_form, id in object_examples:
            print(f"ID: {id}, Form: {form}, Parent Form: {head_form}")

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
