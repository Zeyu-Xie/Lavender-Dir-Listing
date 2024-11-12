# Lavender-Dir-Listing

A GitHub workflow for listing repositories' files.

## Usage

Lavender-Dir-Listing requires two parameters: `FROM` and `DESTINATION`.

`FROM` specifies the directory to list files from.

`DESTINATION` specifies where to save the listing.

```yaml
- name: Generate Directory Listings
    uses: Zeyu-Xie/Lavender-Dir-Listing@[version]
    with:
        FROM: [From which directory to list files]
        DESTINATION: [Where to save the listing]
```

## Dependencies

This action relies on docker image `acanxie/lavender-dir-listing` to generate directory listings. The current version of the image is `1.0.0`, available on linux-amd64 and linux-arm64.
