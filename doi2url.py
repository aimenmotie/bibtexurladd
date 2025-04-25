import re
from typing import List, Dict

def add_urls_from_doi(bib_file_path: str, output_file_path: str) -> None:
    """
    Add URL fields to BibTeX entries based on their DOI.
    
    Args:
        bib_file_path: Path to the input BibTeX file
        output_file_path: Path to save the updated BibTeX file
    """
    with open(bib_file_path, 'r', encoding='utf-8') as file:
        bib_content = file.read()
    
    # Split into individual entries
    entries = re.split(r'(?=@\w+{)', bib_content)
    entries = [entry.strip() for entry in entries if entry.strip()]
    
    updated_entries = []
    
    for entry in entries:
        # Check if entry already has a URL
        has_url = re.search(r'url\s*=\s*{', entry, re.IGNORECASE) is not None
        
        if not has_url:
            # Find DOI in the entry
            doi_match = re.search(r'doi\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
            if doi_match:
                doi = doi_match.group(1).strip()
                # Remove any existing URL prefix from DOI
                doi = doi.replace('https://doi.org/', '').replace('http://doi.org/', '').replace('doi.org/', '')
                
                # Construct the DOI URL
                doi_url = f'https://doi.org/{doi}'
                
                # Find where to insert the URL (before the closing brace)
                closing_brace_pos = entry.rfind('}')
                if closing_brace_pos > 0:
                    # Insert URL before the closing brace
                    updated_entry = entry[:closing_brace_pos].rstrip()
                    # Remove trailing comma if present
                    if updated_entry.endswith(','):
                        updated_entry = updated_entry[:-1]
                    # Add URL field
                    updated_entry += f',\n  url = {{{doi_url}}}' + entry[closing_brace_pos:]
                    entry = updated_entry
        
        updated_entries.append(entry)
    
    # Write to output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(updated_entries))
    
    print(f"Successfully added URLs based on DOIs. Output saved to {output_file_path}")

# Example usage
if __name__ == "__main__":
    input_file = r'C:\Users\pc\Downloads\references.bib'
    output_file = r'C:\Users\pc\Downloads\references_with_urls.bib'
    add_urls_from_doi(input_file, output_file)