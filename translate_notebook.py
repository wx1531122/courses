import nbformat
from googletrans import Translator
import re

def translate_text(text, dest_lang='zh-cn'):
    translator = Translator()
    # Split text into segments that are less than 5000 characters
    # as googletrans has a limit of 5k characters per request
    segments = []
    current_segment = ""
    for paragraph in text.split('\n'):
        if len(current_segment) + len(paragraph) + 1 < 5000:
            current_segment += paragraph + '\n'
        else:
            segments.append(current_segment)
            current_segment = paragraph + '\n'
    segments.append(current_segment)

    translated_segments = []
    for segment in segments:
        if segment.strip(): # Ensure segment is not just whitespace
            try:
                translated_segments.append(translator.translate(segment, dest=dest_lang).text)
            except Exception as e:
                print(f"Error translating segment: {e}")
                translated_segments.append(segment) # Keep original if translation fails
        else:
            translated_segments.append(segment) # Keep whitespace segment as is

    return "\n".join(translated_segments)

def process_notebook(notebook_path):
    # Read the notebook
    notebook = nbformat.read(notebook_path, as_version=4)

    # Iterate over cells
    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            original_source = cell.source

            # Skip if already translated
            if '--- \n### 中文翻译：\n' in original_source or '### 中文翻译：\n' in original_source :
                continue

            # Preserve code blocks and URLs
            code_blocks = re.findall(r'(```.*?```|`.*?`)', original_source, re.DOTALL)
            urls = re.findall(r'\[.*?\]\(.*?\)', original_source) # Markdown links
            html_tags = re.findall(r'<.*?>', original_source) # HTML tags

            # Placeholder for code blocks, URLs, and HTML tags
            placeholder_code = "||CODE_BLOCK_PLACEHOLDER_{}||"
            placeholder_url = "||URL_PLACEHOLDER_{}||"
            placeholder_html = "||HTML_PLACEHOLDER_{}||"

            temp_source = original_source
            # Create a list of all placeholders and their original values
            placeholders = []
            for i, block in enumerate(code_blocks):
                placeholders.append({'placeholder': placeholder_code.format(i), 'original': block})
                temp_source = temp_source.replace(block, placeholder_code.format(i), 1) # Replace only the first occurrence
            for i, url in enumerate(urls):
                placeholders.append({'placeholder': placeholder_url.format(i), 'original': url})
                temp_source = temp_source.replace(url, placeholder_url.format(i), 1) # Replace only the first occurrence
            for i, tag in enumerate(html_tags):
                placeholders.append({'placeholder': placeholder_html.format(i), 'original': tag})
                temp_source = temp_source.replace(tag, placeholder_html.format(i), 1) # Replace only the first occurrence

            # Translate the text
            translated_text = translate_text(temp_source)

            # Restore code blocks, URLs, and HTML tags
            for item in placeholders:
                translated_text = translated_text.replace(item['placeholder'], item['original'], 1) # Replace only the first occurrence

            # Append the translation
            cell.source = f"{original_source}\n\n---\n### 中文翻译：\n{translated_text}"

    # Write the modified notebook
    nbformat.write(notebook, notebook_path)

if __name__ == '__main__':
    notebook_path = 'prompt_evaluations/01_intro_to_evals/01_intro_to_evals.ipynb'
    process_notebook(notebook_path)
    print(f"Notebook '{notebook_path}' has been translated.")
