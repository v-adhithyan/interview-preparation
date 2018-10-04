"""Recursively calculate folder size."""
import os


def folder_size(path):
    """Calculate folder size recursively."""
    total = os.path.size(path)
    if os.path.isdir(path):
        for f in os.listdir(path):
            child = os.path.join(path, f)
            total += folder_size(child)

    return total


def main():
    """Main."""
    path = "/Users/adhi/dev/inter/interview-preparation"
    total = folder_size(path)
    print("{} size is {}".format(path, total))


if __name__ == "__main__":
    main()
