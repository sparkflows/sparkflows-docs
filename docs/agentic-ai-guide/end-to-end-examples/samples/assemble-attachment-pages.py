def main(items, inputs, outputs):
    current = outputs.get("4", {}).get("fields", {})
    filename = current.get("filename")
    if not filename or not items:
        raise ValueError("The current attachment and its text pages are required")
    pages = []
    seen = set()
    for item in items:
        if item.get("fileName") != filename:
            raise ValueError("The text belongs to a different attachment")
        page = item.get("pageNumber")
        content = item.get("content")
        if isinstance(page, bool) or not isinstance(page, int) or page < 1 or page in seen:
            raise ValueError("Every page needs a distinct positive pageNumber")
        if not isinstance(content, str) or not content.strip():
            raise ValueError("This page has no readable text; review the PDF before continuing")
        seen.add(page)
        pages.append((page, content.strip()))
    if seen != set(range(1, len(pages) + 1)):
        raise ValueError("The extracted page sequence is incomplete")
    text = "\n\n".join(content for page, content in sorted(pages))
    if len(text) > 12000:
        raise ValueError("Use the small practice PDFs; this example does not truncate long documents")
    return [{"file_name": filename, "document_text": text, "page_count": len(pages)}]
