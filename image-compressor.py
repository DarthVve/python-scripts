from PIL import Image
import os

def compress_image(input_path, output_path, target_ratio=0.5, output_format="WEBP", max_attempts=10):
    """
    Compress an image.
        - WEBP: lossless first, then near-lossless fallback if target size not reached
        - PNG: strictly lossless
        - Others: saved as-is (no quality fallback)

    Args:
        input_path (str): Path to the source image.
        output_path (str): Path to save the compressed image.
        target_ratio (float): Desired ratio (0.5 = ~50% of original size).
        output_format (str): "WEBP", "PNG", or other supported formats.
        max_attempts (int): Max attempts for near-lossless WEBP fallback.
    """
    original_size = os.path.getsize(input_path)
    target_size = int(original_size * target_ratio)

    img = Image.open(input_path)

    if output_format.upper() == "WEBP":
        # Try lossless WebP first
        img.save(output_path, "WEBP", lossless=True, method=6)
        compressed_size = os.path.getsize(output_path)

        if compressed_size <= target_size:
            print(f"✅ WEBP lossless: {compressed_size/original_size:.2%} of original size")
            return

        # Fallback → near-lossless WebP
        quality = 100
        attempts = 0
        while compressed_size > target_size and attempts < max_attempts and quality > 10:
            quality -= 10
            img.save(output_path, "WEBP", quality=quality, method=6)
            compressed_size = os.path.getsize(output_path)
            attempts += 1

        print(f"⚠️ WEBP near-lossless: {compressed_size/original_size:.2%} of original size (quality={quality})")

    elif output_format.upper() == "PNG":
        # Strictly lossless PNG
        img.save(output_path, "PNG", optimize=True)
        compressed_size = os.path.getsize(output_path)
        print(f"✅ PNG lossless: {compressed_size/original_size:.2%} of original size")

    else:
        # Other formats saved without lossy fallback
        img.save(output_path, output_format.upper())
        compressed_size = os.path.getsize(output_path)
        print(f"ℹ️ {output_format.upper()} saved: {compressed_size/original_size:.2%} of original size")
