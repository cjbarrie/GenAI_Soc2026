# Colab fallback

Colab is supported as an access route, not maintained as a second curriculum.

1. Download the target `.ipynb`, its `data/sessionXX` folder if present, and the weekly task.
2. Upload them under one Colab folder.
3. Replace the repository-location cell with `REPO_ROOT = Path("/content/your-folder")`.
4. Use the live OpenRouter route. Colab cannot normally reach Ollama running on a student laptop, so the required early Ollama calls are completed in local Jupyter or on an in-class paired/instructor machine. Use a recorded return only when access fails.
5. Enter the shared key with the hidden-input cell or store it in Colab Secrets as `OPENROUTER_API_KEY`; never type, print or read it aloud in the recording.
6. Download the completed notebook before the runtime expires.

The completion standard is the same in every environment: a narrated screen recording showing both runs and explaining each operation's input and output, the methodological limit and the reading connection. Upload it by 5:00 p.m. Eastern on the Tuesday before the next class, using the Box link and platform guidance in `coursebook/recording-and-submission.qmd`.
