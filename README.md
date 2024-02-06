# Lavender Dir Listing

## Quick Start

Add this code to your ```.github/workflows/[your workflow name].yml```

```
- name: Generate Directory Listings
  uses: Zeyu-Xie/Lavender-Dir-Listing@v1
  with:
    FOLDER: .
```

Full Code is as below

```
name: Example Using Lavender Dir Listing Version 1.0.0

on: [push]

jobs:

  # Job 1. Generate the Artifact
  pages_directory_listing:

    runs-on: ubuntu-latest
    name: Pages Directory Listing

    steps:

      # Step 1. Checkout Repository
      - name: Checkout Repository
        uses: actions/checkout@v1
        with:
          # branch to check out
          ref: main

      # Step 2. Generate the artifact
      - name: Generate Directory Listings
        uses: Zeyu-Xie/Lavender-Dir-Listing@v1.0.0
        with:
          # directory to generate the artifact
          FOLDER: .
          
      # Step 3. Upload Pages Artifact
      - name: Upload Pages Artifact
        uses: actions/upload-pages-artifact@v2
        with:
          name: github-pages
          path: .
          
  # Job 2. Deploy the Artifact
  deploy_the_artifact:

    needs: pages_directory_listing
    
    permissions:
      pages: write
      id-token: write

    runs-on: ubuntu-latest
    name: Deploy the Artifact
    
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:

      # Step 1. Deploy to GitHub Pages
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1          
```

## Input

The ```With``` property supports following items.

| Item         | Explaination                       | Example            | Default |
| ------------ | ---------------------------------- | ------------------ | ------- |
| ```FOLDER``` | Directory to Generate the Artifact | ```FOLDER: docs``` | ```.``` |

