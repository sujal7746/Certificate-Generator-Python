import cv2

list_of_name = []

def cleanup_data():
    with open("name-list-data.txt") as file:
        for line in file:
            list_of_name.append(line.strip())

def generate_certificates():
    for index, name in enumerate(list_of_name):
        template = cv2.imread("certificate-template.jpg")
        cv2.putText(template, name, (1300, 1500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 5, (0,0,255),5, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template)
        print(f'Processing {index + 1} / {len(list_of_name)}')

cleanup_data()
generate_certificates()
