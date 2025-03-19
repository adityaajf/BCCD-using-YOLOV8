import os
import xml.etree.ElementTree as ET

def xml_to_yolo(xml_file, output_dir, img_width=640, img_height=640):
    """
    Converts a Pascal VOC XML file to YOLO format.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract image dimensions (if available in XML)
    size = root.find('size')
    if size is not None:
        img_width = int(size.find('width').text)
        img_height = int(size.find('height').text)

    yolo_annotations = []
    for obj in root.findall('object'):
        label = obj.find('name').text
        class_id = {'WBC': 0, 'RBC': 1, 'Platelets': 2}[label]

        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        # Normalize bounding box coordinates to [0, 1]
        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    # Save to .txt file
    filename = os.path.splitext(os.path.basename(xml_file))[0] + '.txt'
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write('\n'.join(yolo_annotations))

# Example usage
xml_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/BCCD/Annotations'  # Path to the Annotations folder
yolo_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/BCCD/labels'      # Output directory for YOLO labels
os.makedirs(yolo_dir, exist_ok=True)

for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        xml_to_yolo(os.path.join(xml_dir, xml_file), yolo_dir)