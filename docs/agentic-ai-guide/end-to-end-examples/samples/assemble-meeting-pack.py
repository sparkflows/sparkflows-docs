def main(items, inputs, outputs):
    expected = outputs.get("3", {}).get("items", [])
    if not expected or len(items) != len(expected):
        raise ValueError("One completed brief is required for every selected meeting")
    originals = {meeting["meeting_id"]: meeting for meeting in expected}
    sections = []
    seen = set()
    for record in items:
        meeting_id = record.get("meeting_id")
        original = originals.get(meeting_id)
        if original is None or meeting_id in seen:
            raise ValueError("Missing, repeated or unexpected meeting ID")
        for field in ("meeting_title", "customer_id", "start", "end", "time_zone"):
            if record.get(field) != original.get(field):
                raise ValueError("The brief has mismatched " + field)
        brief = record.get("brief")
        if not isinstance(brief, str) or not brief.strip() or "${" in brief:
            raise ValueError("A non-empty brief is required")
        seen.add(meeting_id)
        sections.append(record["meeting_title"] + " — " + record["customer_id"]
                        + "\n" + record["start"] + " to " + record["end"]
                        + " " + record["time_zone"] + "\n\n" + brief.strip())
    return [{"report": "Practice meeting pack — 6 October 2026\n\n"
                       + "\n\n---\n\n".join(sections),
             "meeting_count": len(sections)}]
