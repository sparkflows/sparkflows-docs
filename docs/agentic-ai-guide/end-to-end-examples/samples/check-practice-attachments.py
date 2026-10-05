def main(items, inputs, outputs):
    expected = {"practice-workshop.pdf", "practice-checklist.pdf"}
    if len(items) != 2 or {item.get("filename") for item in items} != expected:
        raise ValueError("Use exactly the two named practice PDF attachments")
    seen = set()
    result = []
    for item in items:
        message_id = item.get("messageId")
        path = item.get("path")
        if not isinstance(message_id, str) or not message_id.strip():
            raise ValueError("Each attachment needs its source messageId")
        if not isinstance(path, str) or not path.lower().endswith(".pdf"):
            raise ValueError("Each attachment needs the downloaded PDF path")
        if item.get("save_status") not in ("saved", "skipped"):
            raise ValueError("Check the attachment download status")
        source_key = message_id + "|" + item["filename"]
        if source_key in seen:
            raise ValueError("Repeated attachment identity")
        seen.add(source_key)
        result.append({**item, "source_key": source_key})
    return sorted(result, key=lambda item: item["filename"])
