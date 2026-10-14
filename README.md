# Guitar Shop Publishing Snapshot

## Academic Context

University: University of Melbourne  
Course: Publishing/history copy of GuitarShop  
Year: See source project and original Git dates  
Project type: publishing repository


## Overview

A GitHub Pages publishing/history copy of the original handwritten GuitarShop static website.

## Original Context

Chen Jiang’s original publishing repository. Its original default branch is master and remains master; source-page assets matched the GuitarShop pre-maintenance copy. The preserved pre-maintenance snapshot is `e4143c534b8d90c368a6a7e407ba599922ebc6b2`;
its most recent original commit is dated 2022-01-18. This date describes Git evidence,
not necessarily the complete implementation period.

## What I Implemented

Published copies of the store’s eight HTML page types and their styles, scripts and images.

## Technical Approach

[GuitarShop](https://github.com/chenjiang0819/GuitarShop) is the canonical maintained source project. This repository keeps the original publishing copy and adds a root index redirect into home.html.

The historical master default is preserved. Source UI maintenance has not been independently duplicated into this publishing snapshot.

## Build / Run

Run `python3 -m http.server 8000 --bind 127.0.0.1` and open the root URL. For browser checks, install `requirements-dev.txt` in a venv with local Chrome, then run `python3 -B -m unittest discover -s tests -v`. GitHub Pages configuration/deployment is not independently verified by the local checks.

## Testing

- Local Chrome root redirects to home.html. All nine URLs loaded at desktop, tablet and mobile widths without page errors, missing local assets or broken images.
- Publishing regression tests verify root behavior and desktop page/assets navigation.
- Original tablet overflow and missing control labels remain documented; they are improved in GuitarShop rather than independently duplicated here.
- Evidence: chenjiang0819.github.io_browser_publishing.json and publishing test log.

## 2026 Maintenance

- Added index.html so root requests enter the home page.
- Documented the publishing/source relationship, local launch, actual verification and historical limitations.
- Added a local Chrome publishing test for root navigation and all local page assets.

The later work is AI-assisted maintenance, separate from the original implementation.
The exact original snapshot remains on `archive/handwritten-original`.
See [AI_PROJECT_REVIEW.md](AI_PROJECT_REVIEW.md) for a technical review.

## Known Limitations

- This remains the original publishing/history copy, with original tablet overflow and incomplete keyboard/control labelling. Use GuitarShop for maintained source behavior.
- No commerce backend exists. External fonts and live GitHub Pages deployment were not verified.
