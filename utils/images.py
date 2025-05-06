from pathlib import Path
from PIL import Image
import os

widths = [300, 600, 900]


def optimize_image(source_path, output_dir):
    img = Image.open(source_path)
    filename = Path(source_path).stem

    # Convert to RGB if the image is in RGBA mode (handles PNG transparency)
    if img.mode in ("RGBA", "LA"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])  # Use the alpha channel as mask
        img = background

    for width in widths:
        # Calculate height maintaining aspect ratio
        ratio = width / img.size[0]
        height = int(img.size[1] * ratio)

        resized = img.resize((width, height), Image.Resampling.LANCZOS)
        output_path = os.path.join(output_dir, f"{filename}-{width}w.jpg")

        # Always save as JPEG with optimization
        resized.save(output_path, "JPEG", quality=85, optimize=True)


def process_all_images():
    source_dir = Path(os.path.expanduser("~/Documents/img_src"))
    output_dir = Path("../static/images")

    output_dir.mkdir(parents=True, exist_ok=True)

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return

    # Process both jpg and png files
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        for image_path in source_dir.glob(ext):
            optimize_image(image_path, output_dir)


if __name__ == "__main__":
    process_all_images()
