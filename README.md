# Evade Tracker build orchestration

This public repository contains build orchestration only. The application
source remains private in `umbra-me/tracker-evade-fail-apple`. Workflows accept
an exact source commit and use a short-lived token from the repository-scoped,
read-only GitHub App. No source, signing material, IPA, or raw private build
logs are published.

- `build.yml` runs shared tests and all four unsigned simulator builds.
- `testflight.yml` validates signing assets, archives the iPhone app with its
  Watch companion and both widget extensions, verifies the signed archive, and
  uploads it to App Store Connect.

## Provisioning status

All ten non-secret project and signing-name variables are configured. The
encrypted private-source credential, diagnostic key, signing certificate and
profiles, and App Store Connect API credential remain intentionally unset, so
the workflows cannot yet access source or produce a signed release. Current
TestFlight uploads use the direct local Xcode archive path.

App Store Connect app `6807693312` has processed Evade Tracker `0.0.1 (1)` and
persistent-login build `0.0.1 (2)`; both are assigned to the Personal Testing
group. Tester identities and invitation links are never stored here.
