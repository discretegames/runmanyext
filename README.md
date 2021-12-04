# [RunMany Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

[RunMany](https://pypi.org/project/runmany/) is a tool that lets you write and run programs in multiple languages
from one file. This extension provides quick ways to run RunMany files (file extension `.many` or `.runmany`) in VSCode, as well as syntax highlighting for RunMany files and 42
[embeddable programming languages](https://github.com/discretegames/runmanyext/blob/main/supported-languages.csv):

> Ada,
> ARM,
> Bash,
> Batch,
> C,
> C#,
> Clojure,
> COBOL,
> C++,
> Dart,
> Erlang,
> Fortran,
> F#,
> Go,
> Groovy,
> Haskell,
> Java,
> JavaScript,
> Julia,
> Kotlin,
> Lisp,
> Lua,
> MIPS,
> Objective-C,
> OCaml,
> Pascal,
> Perl,
> PHP,
> PowerShell,
> Python,
> Python 2,
> R,
> Racket,
> Ruby,
> Rust,
> Scala,
> Scheme,
> Swift,
> TypeScript,
> x86,
> VBScript,
> Visual Basic

Languages not [built into VSCode](https://github.com/microsoft/vscode/tree/main/extensions) such as Ada and Pascal
require their own respective VSCode extensions to be installed for their syntax highlighting to work in RunMany files.

RunMany syntax highlighting in action on a
[sample file](https://github.com/discretegames/runmanyext/blob/main/exampleWorkspace/sample.many):

![syntax highlighting sample](https://raw.githubusercontent.com/discretegames/runmanyext/main/images/sample.png)

## Usage

This extension is intended to be used alongside the [RunMany Python package](https://pypi.org/project/runmany/), which is the tool that actually runs `.many` files.

Install the package for [Python 3.6 and above](https://www.python.org/downloads/) with

```text
pip install runmany
```

in terminal, or [see more installation information here](https://github.com/discretegames/runmany#installation).

Then simply hit F5 (or your normal run/debug keybind) in VSCode to run the currently focused RunMany
file in an integrated terminal.

There are additional run buttons on the title menu and command palette.
You can also add a RunMany launch configuration to the [.vscode/launch.json](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) file of your workspace. For example, this would go in the `"configurations"` array:

```json
{
    "name": "RunMany: Run Current File",
    "type": "runmany",
    "request": "launch",
    "program": "${file}",
    "settingsFile": "",
    "outputFile": ""
}
```

See [here for a full launch.json example](https://github.com/discretegames/runmanyext/blob/main/exampleWorkspace/.vscode/launch.json)
 in an
[example workspace](https://github.com/discretegames/runmanyext/tree/main/exampleWorkspace).

The optional properties `"settingsFile"` and `"outputFile"` correspond to the command line arguments for the
settings JSON and output redirect of the RunMany Python package.

Learn more about the RunMany Python package, including RunMany syntax and what can go in the settings JSON,
on [PyPI](https://pypi.org/project/runmany/)
or [GitHub](https://github.com/discretegames/runmany), or look at some
[example files](https://github.com/discretegames/runmany/tree/main/examples).

## Limitations

Until [Language Server Protocol 3.17](
https://microsoft.github.io/language-server-protocol/specifications/specification-3-17/)
is released there is unfortunately
[no reasonable way](https://code.visualstudio.com/api/language-extensions/embedded-languages#conclusion)
to have underlined errors and warnings (knows as diagnostics) show up in embedded code in VSCode.
Putting the work into support things like autocompletion or semantic highlighting for embedded languages
does not seem worth it without being able to implement diagnostics at the same time,
since they would be the most useful feature.

So for for now, this extension only provides syntax highlighting and easy ways to run RunMany files,
no diagnostics or other features.

## Resources

- [Change Log](https://marketplace.visualstudio.com/items/discretegames.runmany/changelog)

- [GitHub Repo](https://github.com/discretegames/runmanyext)

- [Marketplace Page](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

- [RunMany Python Package on PyPI](https://pypi.org/project/runmany/)

- [RunMany Python Package on GitHub](https://github.com/discretegames/runmany)

- [Example RunMany Workspace](https://github.com/discretegames/runmanyext/tree/main/exampleWorkspace)
