def main(items, inputs, outputs):
    meetings = []
    seen = set()
    for event in items:
        subject = str(event.get("subject") or "")
        if not subject.startswith("[DOCS ") or event.get("isCancelled") is True:
            continue
        match = re.fullmatch(r"\[DOCS (C-[0-9]{3})\] (.+)", subject)
        if not match:
            raise ValueError("Use a subject such as [DOCS C-001] Kickoff")
        event_id = event.get("id")
        if not isinstance(event_id, str) or not event_id or event_id in seen:
            raise ValueError("Every meeting needs a unique event ID")
        if event.get("timeZone") != "UTC":
            raise ValueError("Set Show times in to UTC in the calendar read")
        start = str(event.get("start") or "")
        end = str(event.get("end") or "")
        if not start.startswith("2026-10-06T") or not end.startswith("2026-10-06T"):
            raise ValueError("This exercise uses meetings on 6 October 2026")
        start = re.sub(r"(\.[0-9]{6})[0-9]+", r"\1", start)
        end = re.sub(r"(\.[0-9]{6})[0-9]+", r"\1", end)
        start_time = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_time = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
        if end_time <= start_time:
            raise ValueError("The meeting must end after it starts")
        seen.add(event_id)
        meetings.append({"meeting_id": event_id, "meeting_title": match.group(2),
                         "customer_id": match.group(1), "start": start,
                         "end": end, "time_zone": "UTC"})
    if not meetings or len(meetings) > 2:
        raise ValueError("Keep one or two [DOCS ...] meetings for this exercise")
    return sorted(meetings, key=lambda meeting: (meeting["start"], meeting["meeting_id"]))
