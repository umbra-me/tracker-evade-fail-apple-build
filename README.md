# Evade Tracker build orchestration

This public repository contains build orchestration only. The application
source remains private in `umbra-me/tracker-evade-fail-apple`. Workflows accept an
exact source commit and use a short-lived token from the repository-scoped,
read-only GitHub App. No source, signing material, IPA, or
raw private build logs are published.

- `build.yml` runs shared tests and all four unsigned simulator builds.
- `testflight.yml` validates signing assets, archives the iPhone app with its
  Watch companion and both widget extensions, verifies the signed archive, and
  uploads it to App Store Connect.
