# Markdown SmartBreaks

A slightly better `nl2br` extension for Python Markdown.

## Whats different?
- Won't break for html tags. (e.g. code blocks)

## Installation

``` bash
pip install markdown-smartbreaks
```

## Usage

### Markdown module
``` python
import markdown
import smartbreaks

data = markdown.markdown(
    md,
    extensions=[
        smartbreaks.SmartBreaksExtension()
    ]
)
```

### MkDocs `mkdocs.yml`
``` yaml
markdown_extensions:
  - smartbreaks
```

## License

Licensed under the MIT License.
