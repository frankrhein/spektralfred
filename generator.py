from PIL import Image
import os

def resize_img(folder):
    # Minimum short side length (pixels)
    min_short_side = 800

    for filename in os.listdir(folder):
        if filename.lower().endswith('.jpg'):
            path = os.path.join(folder, filename)
            with Image.open(path) as img:
                width, height = img.size
                short_side = min(width, height)

                if short_side > min_short_side:
                    # Calculate new size preserving aspect ratio
                    if width < height:
                        new_width = min_short_side
                        new_height = int((min_short_side / width) * height)
                    else:
                        new_height = min_short_side
                        new_width = int((min_short_side / height) * width)

                    resized = img.resize((new_width, new_height), Image.LANCZOS)
                    resized.save(path)  # Overwrite original, or change filename to save separately
                    print(f'Resized {filename} to {new_width}x{new_height}')
                # else:
                #     print(f'Skipped {filename}, already smaller than threshold')

def generate_image_list(folder):
    output_file = os.path.join(folder, 'imagelist.txt')

    # List all JPG files and sort alphabetically
    images = sorted([f for f in os.listdir(folder) if f.lower().endswith('.jpg')])

    with open(output_file, 'w') as f:
        for img in images:
            f.write(f"{img}\n")

    print(f"Saved {len(images)} image filenames to {output_file}")

def run_all_folders(folderlist):

    for folder in folderlist:
        resize_img(folder)
        generate_image_list(folder)

if __name__ == '__main__':

    assets_dir = './assets'

# List all subdirectories in ./assets
    subfolders = [
        os.path.join(assets_dir, name).replace('\\', '/')
        for name in os.listdir(assets_dir)
        if os.path.isdir(os.path.join(assets_dir, name))
    ]

    print('Processing these folders:', subfolders)
    run_all_folders(subfolders)