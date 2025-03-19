import os
import shutil

def organize_dataset(image_sets_dir, jpeg_images_dir, labels_dir, output_dir):
    """
    Organizes images and labels into train, val, and test sets.
    """
    splits = ['train', 'val', 'test']
    for split in splits:
        os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)

        split_file = os.path.join(image_sets_dir, 'Main', f'{split}.txt')
        with open(split_file, 'r') as f:
            for line in f:
                img_name = line.strip()
                img_path = os.path.join(jpeg_images_dir, f'{img_name}.jpg')
                label_path = os.path.join(labels_dir, f'{img_name}.txt')

                if os.path.exists(img_path) and os.path.exists(label_path):
                    shutil.copy(img_path, os.path.join(output_dir, 'images', split))
                    shutil.copy(label_path, os.path.join(output_dir, 'labels', split))

# Example usage
image_sets_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/BCCD/ImageSets'
jpeg_images_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/BCCD/JPEGImages'
labels_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/BCCD/labels'
output_dir = '/Users/adityapnv/Desktop/Documents/YOLO-BCCD/yolo_format'

organize_dataset(image_sets_dir, jpeg_images_dir, labels_dir, output_dir)