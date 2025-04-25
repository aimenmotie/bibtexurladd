DOI to URL Converter for BibTeX Files
Automatically add proper URL fields to BibTeX entries using DOI identifiers

📖 Overview
This Python script processes BibTeX bibliography files to:

Identify entries that have DOI (Digital Object Identifier) fields but are missing URL fields

Generate proper https://doi.org/ URLs from the DOI values

Add these URLs to the BibTeX entries while preserving all existing formatting

Perfect for researchers, academics, and anyone working with bibliographic data who wants to ensure their references contain clickable links to source materials.

✨ Key Features
Smart DOI Detection: Finds DOIs even if they're formatted with different prefixes

URL Generation: Creates standardized https://doi.org/ URLs

Format Preservation: Maintains all existing BibTeX formatting and fields

Duplicate Prevention: Only adds URLs to entries that don't already have one

Large File Support: Efficiently processes bibliographies with thousands of entries

Command Line Interface: Easy integration into automated workflows

🛠 Technical Details
Pure Python: No external dependencies required

Robust Parsing: Handles various BibTeX formatting styles

Unicode Support: Properly processes international characters

Error Resilient: Skips malformed entries without failing

📚 Example
Input BibTeX:

bibtex
@article{example2023,
  author = {Doe, John},
  title = {Example Article},
  journal = {Journal of Examples},
  year = {2023},
  doi = {10.1234/example.2023}
}
Output BibTeX:

bibtex
@article{example2023,
  author = {Doe, John},
  title = {Example Article},
  journal = {Journal of Examples},
  year = {2023},
  doi = {10.1234/example.2023},
  url = {https://doi.org/10.1234/example.2023}
}
🚀 Getting Started
Installation
bash
git clone https://github.com/yourusername/doi2url.git
cd doi2url
Basic Usage
bash
python doi2url.py input.bib output.bib
Advanced Options
Process files in place (using temporary file):

bash
python doi2url.py my_references.bib my_references.bib
Pipe input/output:

bash
cat input.bib | python doi2url.py - - > output.bib
🤝 Contributing
We welcome contributions! Please see our Contribution Guidelines for details.

📜 License
MIT License - See LICENSE for full text.

Usage
Basic command:

bash
python doi2url.py input.bib output.bib
Example:

bash
python doi2url.py references.bib references_with_urls.bib
Requirements
Python 3.7+

No external dependencies

License
This project is licensed under the MIT License - see the LICENSE file for details.






