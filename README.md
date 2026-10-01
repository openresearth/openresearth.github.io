# ore · Open Resources for Earth Sciences

Source for the website **https://openresearth.github.io**: free online workshops and
open learning resources for geoscience students.

All pages are Markdown files in the [`docs/`](docs/) folder. When a change is merged
into `main`, GitHub builds the site with Sphinx and publishes it automatically.

## Where things live

| To change… | Edit |
|------------|------|
| Home page | `docs/index.md` |
| Workshop list | `docs/workshops/index.md` |
| A new workshop | copy `docs/workshops/_template.md` |
| Resource lists | `docs/resources/*.md` |
| Sidebar sections | the `toctree` blocks at the end of `docs/index.md` |
| Colours and fonts | `docs/_static/custom.css` |
| Site settings | `docs/conf.py` |

See [Contributing](docs/community/contributing.md) for step-by-step instructions.

## Preview the site on your computer

```bash
pip install -r requirements.txt sphinx-autobuild
sphinx-autobuild docs docs/_build/html
```

Then open http://127.0.0.1:8000. The page reloads each time you save a file.

## License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
