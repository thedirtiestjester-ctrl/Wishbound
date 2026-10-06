# Android build instructions

Target: Ren'Py 8.5.3 (or a later compatible Ren'Py 8 release).

1. Install the Ren'Py 8.5.3 SDK.
2. Place the `Wishbound_v0.1` folder inside the Ren'Py projects directory or add its parent folder as a projects directory.
3. Launch Ren'Py and select **Wishbound: Her Morning**.
4. Choose **Android**. Ren'Py will install/configure RAPT if needed.
5. In Android settings, use package name `com.wishbound.hermorning` (already declared in options.rpy where supported).
6. Choose **Build Package** to create the APK/AAB.

The official Ren'Py 8.5.3 release provides a separate RAPT Android support package.

For a release build, replace the placeholder art, set signing credentials, review store content ratings, and test on real Android hardware.
