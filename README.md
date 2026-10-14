# Guitar Shop Publishing Snapshot

A GitHub Pages publishing/history copy of the original handwritten GuitarShop static website.

Chen Jiang’s historical publishing copy; [GuitarShop](https://github.com/chenjiang0819/GuitarShop) is the maintained source.

University: University of Melbourne  
Course: Publishing/history copy of GuitarShop  

## Implementation

Published copies of the store’s eight HTML page types and their styles, scripts and images.

## Technical approach

[GuitarShop](https://github.com/chenjiang0819/GuitarShop) is the canonical maintained source project. This repository keeps the original publishing copy and adds a root index redirect into home.html.

The historical master default is preserved. Source UI maintenance has not been independently duplicated into this publishing snapshot.

## Run

Run `python3 -m http.server 8000 --bind 127.0.0.1` and open the root URL. For browser checks, install `requirements-dev.txt` in a venv with local Chrome, then run `python3 -B -m unittest discover -s tests -v`.

## Checks and results

- Local Chrome root redirects to home.html. All nine URLs loaded at desktop, tablet and mobile widths without page errors, missing local assets or broken images.
- Publishing regression tests verify root behavior and desktop page/assets navigation.
- Original tablet overflow and missing control labels remain documented; they are improved in GuitarShop rather than independently duplicated here.

## 2026 maintenance

- Added index.html so root requests enter the home page.
- Documented the publishing/source relationship, local launch, actual verification and historical limitations.
- Added a local Chrome publishing test for root navigation and all local page assets.

These changes are 2026 AI-assisted maintenance of the original student implementation.

## Usage notes

- This remains the original publishing/history copy, with original tablet overflow and incomplete keyboard/control labelling. Use GuitarShop for maintained source behavior.
