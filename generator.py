from PIL import Image
import os

def resize_img(read_folder, exp_folder):
    # Minimum short side length (pixels)
    min_short_side = 1080

    for filename in os.listdir(read_folder):
        if filename.lower().endswith('.jpg'):            
            read_path = os.path.join(read_folder, filename)
            exp_path = os.path.join(exp_folder, filename)
            with Image.open(read_path) as img:
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
                    resized.save(exp_path)  # Overwrite original, or change filename to save separately
                    print(f'Resized {filename} to {new_width}x{new_height}')
                # else:
                #     print(f'Skipped {filename}, already smaller than threshold')

def generate_image_list(read_folder, exp_folder):
    output_file = os.path.join(exp_folder, 'imagelist.txt')

    # List all JPG files and sort alphabetically
    images = sorted([f for f in os.listdir(read_folder) if f.lower().endswith('.jpg')])

    with open(output_file, 'w') as f:
        for img in images:
            f.write(f"{img}\n")

    print(f"Saved {len(images)} image filenames to {output_file}")

def run_all_folders(read_folderlist, exp_folderlist):

    for i in range(len(read_folderlist)):
        read_folder = read_folderlist[i]
        exp_folder = exp_folderlist[i]
        resize_img(read_folder, exp_folder)
        generate_image_list(read_folder, exp_folder)

if __name__ == '__main__':

    hd_dir = './hd-downloads'
    assets_dir = './assets'

    # List all subdirectories in ./hd_downloads
    read_subfolders = [
        os.path.join(hd_dir, name).replace('\\', '/')
        for name in os.listdir(hd_dir)
        if os.path.isdir(os.path.join(hd_dir, name))
    ]

    # List all subdirectories in ./assets
    exp_subfolders = [
        os.path.join(assets_dir, name).replace('\\', '/')
        for name in os.listdir(assets_dir)
        if os.path.isdir(os.path.join(assets_dir, name))
    ]

    print('Processing these folders:', read_subfolders)
    run_all_folders(read_subfolders, exp_subfolders)