from pathlib import Path
from PIL import Image
import os

widths = [300, 600, 900]


def optimize_image(source_path, output_dir):
    img = Image.open(source_path)
    filename = Path(source_path).stem
    ext = source_path.suffix.lower()

    is_transparent = img.mode in ("RGBA", "LA") or (
        ext == ".png" and "transparency" in img.info
    )

    for width in widths:
        # Calculate height maintaining aspect ratio
        ratio = width / img.size[0]
        height = int(img.size[1] * ratio)

        resized = img.resize((width, height), Image.Resampling.LANCZOS)

        if is_transparent:
            # Ensure resized image maintains transparency
            if resized.mode not in ("RGBA", "LA"):
                resized = resized.convert("RGBA")

            output_path = os.path.join(output_dir, f"{filename}-{width}w.png")
            resized.save(output_path, "PNG", optimize=True)
        else:
            # Convert to RGB if needed (e.g., for JPEG)
            if resized.mode != "RGB":
                resized = resized.convert("RGB")

            output_path = os.path.join(output_dir, f"{filename}-{width}w.jpg")
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
