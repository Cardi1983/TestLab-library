def safe_get_item(db, path):
    try:
        return db.GetItem(path)
    except Exception:
        return None
