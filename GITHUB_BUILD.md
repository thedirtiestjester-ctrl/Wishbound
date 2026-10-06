# GitHub Android build

This repository includes `.github/workflows/android-apk.yml`.

It builds a universal sideload APK on pushes to `main` that change the game/build files, and can also be run manually from **Actions → Build Android APK → Run workflow**.

The CI key is generated fresh for test/sideload builds. Do not use these CI-generated APKs as a Play Store production signing lineage. Before publishing to an app store, replace the temporary key step with repository secrets containing a permanent keystore and passwords.

The workflow uses Ren'Py 8.5.3, RAPT and an Android SDK via `Ayowel/renpy-setup-action@v3`.
