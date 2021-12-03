# Change Log

All notable changes to the
["RunMany" VSCode extension](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)
will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2021-12-03

Updated extension to match new syntax of RunMany version 2.1.0. TODO: update changelog.

## [1.0.2] - 2021-10-19

Removed misleading `RunMany: Current File` launch configuration as VSCode auto-removes the `${file}` from it.

## [1.0.1] - 2021-10-09

Re-added bracket and quote auto-completion for `()` `[]` `{}` `''` `""`.

## [1.0.0] - 2021-09-27

Bumped to 1.0.0 because the project is done for the present.

## [0.0.6] - 2021-09-27

- Added ways to run RunMany files directly in VSCode:
  - By hitting F5 (or run/debug keybind) to run current file directly.
  - On command palette and in title menu.
  - Via launch.json configurations that may optionally have `"settingsFile"` and `"outputFile"`.
- Updated readme describing ways to run.

## [0.0.5] - 2021-09-23

- Fixed issue where comments with characters like quotes or colon would appear to be part of code.
- Tweaked sample file and image.

## [0.0.4] - 2021-09-22

- Fixed readme image link issue that only showed up on marketplace and not github.

## [0.0.3] - 2021-09-22

- Improved readme.
- Added `sample.many` sample file with images.
- Improved icon.

## [0.0.2] - 2021-09-21

- Removed undesired icon theme prompt.
- Improved branding.

## [0.0.1] - 2021-09-21

Initial release.

- Readme.
- RunMany syntax highlighting grammar.
- Syntax highlighting for 34 embedded languages.
- Icon for extension and .many files.
