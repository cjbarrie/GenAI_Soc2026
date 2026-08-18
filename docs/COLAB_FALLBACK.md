# Colab fallback

Colab is supported as an access route, not maintained as a second curriculum.

1. Download the target `.ipynb`, its `data/sessionXX` folder if present, and the weekly task.
2. Upload them under one Colab folder.
3. Replace the repository-location cell with `REPO_ROOT = Path("/content/your-folder")`.
4. Leave `RUN_LIVE = False` for required work.
5. If a demonstration uses OpenRouter, store the key in Colab Secrets as `OPENROUTER_API_KEY`; do not type or print it in the notebook.
6. Download the completed notebook before the runtime expires.

The completion standard is the same in every environment: prediction, working code, interpreted check, and reading-linked claim.

