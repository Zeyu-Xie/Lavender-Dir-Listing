# Lavender-Dir-Listing

A GitHub workflow for listing repositories' files.

## Usage

Lavender-Dir-Listing requires one parameter: `FOLDER`. This parameter specifies the directory to list files from.

```yaml
- name: Generate Directory Listings
  uses: Zeyu-Xie/Lavender-Dir-Listing@[version]
  with:
    FOLDER: [Listed Folder]
```

## Dependencies

This action relies on docker image `acanxie/lavender-dir-listing` to generate directory listings. The current version of the image is `1.0.0`, available on linux-amd64 and linux-arm64.
