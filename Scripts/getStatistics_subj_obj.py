import conllu

def analyze_conllu_file(conllu_file_path):
    # Load the CoNLL-U file
    with open(conllu_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Parse the CoNLL-U data
    sentences = conllu.parse(data)

    # Initialize counts
    total_subjects = 0
    subjects_to_right = 0
    total_objects = 0
    objects_to_left = 0

    # Iterate through sentences
    for sentence in sentences:
        for token in sentence:
            if token["deprel"] == "nsubj":
                total_subjects += 1
                if token["head"] < token["id"]:
                    subjects_to_right += 1
            elif token["deprel"] == "obj":
                total_objects += 1
                if token["head"] > token["id"]:
                    objects_to_left += 1

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

if __name__ == "__main__":
    conllu_file = "C:\\Users\\eleni\\Desktop\\Project Tools\\CappadocianUDs\\AnnotationsFinal\\AnnotationsFinal.conllu"
    analyze_conllu_file(conllu_file)
