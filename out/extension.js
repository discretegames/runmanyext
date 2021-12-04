"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DummyDebugSession = exports.activate = void 0;
const vscode = require("vscode");
const vscode_debugadapter_1 = require("vscode-debugadapter");
let runmanyTerminal;
function getTerminal() {
    if (!runmanyTerminal || runmanyTerminal.exitStatus) {
        runmanyTerminal = vscode.window.createTerminal("RunMany");
    }
    return runmanyTerminal;
}
function activate(context) {
    context.subscriptions.push(vscode.debug.registerDebugConfigurationProvider("runmany", new RunManyConfigurationProvider()), vscode.debug.registerDebugAdapterDescriptorFactory("runmany", new InlineDebugAdapterFactory()), vscode.commands.registerCommand("extension.runmany.run", (resource) => {
        if (!resource && vscode.window.activeTextEditor) {
            resource = vscode.window.activeTextEditor.document.uri;
        }
        if (resource) {
            vscode.debug.startDebugging(undefined, {
                name: "RunMany: Run Current File",
                type: "runmany",
                request: "launch",
                program: resource.fsPath,
            });
        }
    }));
}
exports.activate = activate;
class RunManyConfigurationProvider {
    resolveDebugConfiguration(_folder, config, _token) {
        if (!config.name && !config.type && !config.request) {
            const editor = vscode.window.activeTextEditor;
            if (editor && editor.document.languageId === "many") {
                config.name = "RunMany: Dynamic Launch";
                config.type = "runmany";
                config.request = "launch";
                config.program = "${file}";
                config.settingsFile = "";
                config.outputFile = "";
            }
        }
        if (!config.program) {
            return vscode.window
                .showInformationMessage(`No program found to run for RunMany launch configuration.`)
                .then((_) => {
                return undefined;
            });
        }
        if (!config.settingsFile) {
            config.settingsFile = "";
        }
        if (!config.outputFile) {
            config.outputFile = "";
        }
        return config;
    }
}
class InlineDebugAdapterFactory {
    createDebugAdapterDescriptor(session) {
        const terminal = getTerminal();
        terminal.show();
        const programArg = `"${session.configuration.program}"`;
        const settingsArg = session.configuration.settingsFile && ` -s "${session.configuration.settingsFile}"`;
        const outputArg = session.configuration.outputFile && ` -o "${session.configuration.outputFile}"`;
        terminal.sendText(`runmany ${programArg}${settingsArg}${outputArg}`);
        return new vscode.DebugAdapterInlineImplementation(new DummyDebugSession());
    }
}
class DummyDebugSession extends vscode_debugadapter_1.DebugSession {
    initializeRequest() {
        this.sendEvent(new vscode_debugadapter_1.TerminatedEvent());
    }
}
exports.DummyDebugSession = DummyDebugSession;
//# sourceMappingURL=extension.js.map