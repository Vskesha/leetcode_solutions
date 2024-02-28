def rgb_to_hex(r: int, g: int, b: int) -> str:
    if r > 255 or g > 255 or b > 255 or r < 0 or g < 0 or b < 0:
        raise ValueError("Value out of range [0, 255]")
    return f"{r:02x}{g:02x}{b:02x}"


if __name__ == "__main__":
    print(rgb_to_hex(255, 192, 0))
    assert rgb_to_hex(255, 192, 0) == "ffc000"
    print(rgb_to_hex(0, 128, 255))
    assert rgb_to_hex(0, 128, 255) == "0080ff"
    print("Test passed")
