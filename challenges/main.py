def all_unique_tags(posts):
    tags = set()
    for post in posts:
        tags.update(post["tags"])
    return tags
    
print(all_unique_tags([{"title": "A", "tags": ["python", "web"]}, {"title": "B", "tags": ["web", "css"]}]))