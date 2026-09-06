import os
from mutagen.mp3 import MP3

AUDIO_DIR = r"C:\Users\ASUS\Desktop\audio"


def main():
    total = 0.0
    count = 0
    for i in range(1, 111):
        path = os.path.join(AUDIO_DIR, f"image_{i}.mp3")
        if not os.path.exists(path):
            print(f"missing: image_{i}.mp3")
            continue
        length = MP3(path).info.length
        total += length
        count += 1
    mins, secs = divmod(total, 60)
    print(f"\n{count} files found, total length: {int(mins)}m {secs:.1f}s ({total:.1f} sec)")


if __name__ == "__main__":
    main()
