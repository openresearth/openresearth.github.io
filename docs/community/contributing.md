# Contributing

Thank you for helping! Every page on this site is a plain Markdown file in the
[`docs/` folder](https://github.com/openresearth/openresearth.github.io/tree/main/docs)
of our GitHub repository. No coding is needed.

## Add a resource

1. Open the resource page you want to improve on this site.
2. Click **Edit on GitHub** at the top right.
3. Click the pencil icon, then copy an existing table row and change it:
   ```markdown
   | [Resource name](https://link) | Type | One-line description |
   ```
4. Click **Commit changes…** → **Propose changes**. A maintainer will review it.

## Propose a workshop

1. Copy the [workshop template](https://github.com/openresearth/openresearth.github.io/blob/main/docs/workshops/_template.md).
2. Save it in `docs/workshops/` as `YYYY-MM-short-title.md` and fill it in.
3. Add a row to the "Upcoming" table in `docs/workshops/index.md`.
4. Open a pull request. The page appears in the sidebar automatically.

Prefer not to edit files? Open an issue instead:
[suggest a resource](https://github.com/openresearth/openresearth.github.io/issues/new?template=suggest-resource.md) ·
[propose a workshop](https://github.com/openresearth/openresearth.github.io/issues/new?template=propose-workshop.md)

## Guidelines

- Only **free and open-access** resources (no paywalled links).
- One resource per row, with a short description.
- Check that links work.
- Be respectful and welcoming to everyone.

## Markdown cheat sheet

```markdown
# Heading 1
## Heading 2
**bold**   *italic*
[link text](https://example.com)
- bullet point
1. numbered point
![image description](../_static/image.png)

| Column | Column |
|--------|--------|
| cell   | cell   |
```

Boxes like the "Next workshop" one on the home page are written as:

```markdown
:::{note}
Text inside a highlighted box.
:::
```
