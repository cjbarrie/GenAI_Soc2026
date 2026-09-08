# Colab fallback

Colab is supported as an access route, not maintained as a second curriculum.

1. Use the **Open in Google Colab** button on the week's Python page. Every link must point to the public `cjbarrie/GenAI_Soc2026` repository.
2. Sign into a Google account if Colab asks.
3. Choose **File → Save a copy in Drive** if you want your changes to persist.
4. Run the first setup cell. It installs the `openrouter` and `ollama` Python SDKs if they are missing, clones the public repository into the temporary Colab runtime and moves into the course directory, so accompanying data can be found. The `ollama` SDK can be imported in Colab, but the local Ollama server still cannot be reached there.
5. Use the live OpenRouter route. Colab cannot normally reach Ollama running on a student laptop, so the required early Ollama calls are completed in local Jupyter or on an in-class paired/instructor machine. Use a recorded return only when access fails.
6. Enter the shared key with the hidden-input cell or store it in Colab Secrets as `OPENROUTER_API_KEY`; never type, print or read it aloud in the recording.
7. Download the completed notebook before the runtime expires if you did not save a copy in Drive.

The completion standard is the same in every environment: a narrated screen recording showing both runs and explaining each operation's input and output, the methodological limit and the reading connection. Upload it by 5:00 p.m. Eastern on the Tuesday before the next class, using the Box link and platform guidance in `coursebook/recording-and-submission.qmd`.
