# Validation summary — v0.2

Static validation performed in the build workspace:

- All scripted `jump`/`call` targets resolve to declared labels.
- All image paths declared by the script exist in the project.
- All PNG files pass Pillow image verification.
- The GitHub Actions workflow parses as YAML.
- Six rewritten adult identities are exposed by the reality selector.
- No uploaded commercial Game CG/full-rip archive bytes are included.

A true Ren'Py lint/compile could not be executed locally because the Ren'Py SDK is not installed in the current container and outbound package downloads from the container are blocked. The included GitHub Actions workflow is intended to perform the real Ren'Py/RAPT build on GitHub-hosted runners.
