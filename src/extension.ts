import * as vscode from "vscode";
import { WorkspaceFolder, DebugConfiguration, ProviderResult, CancellationToken } from "vscode";
import { DebugSession, TerminatedEvent } from "vscode-debugadapter";

let runmanyTerminal: vscode.Terminal;

function getTerminal(): vscode.Terminal {
	if (!runmanyTerminal || runmanyTerminal.exitStatus) {
		runmanyTerminal = vscode.window.createTerminal("RunMany");
	}
	return runmanyTerminal;
}

export function activate(context: vscode.ExtensionContext) {
	context.subscriptions.push(
		vscode.debug.registerDebugConfigurationProvider("runmany", new RunManyConfigurationProvider()),
		vscode.debug.registerDebugAdapterDescriptorFactory("runmany", new InlineDebugAdapterFactory()),
		vscode.commands.registerCommand("extension.runmany.run", (resource: vscode.Uri) => {
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
		})
	);
}

class RunManyConfigurationProvider implements vscode.DebugConfigurationProvider {
	resolveDebugConfiguration(
		_folder: WorkspaceFolder | undefined,
		config: DebugConfiguration,
		_token?: CancellationToken
	): ProviderResult<DebugConfiguration> {
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

class InlineDebugAdapterFactory implements vscode.DebugAdapterDescriptorFactory {
	createDebugAdapterDescriptor(session: vscode.DebugSession): ProviderResult<vscode.DebugAdapterDescriptor> {
		const terminal = getTerminal();
		terminal.show();
		const programArg = `"${session.configuration.program}"`;
		const settingsArg = session.configuration.settingsFile && ` -j "${session.configuration.settingsFile}"`;
		const outputArg = session.configuration.outputFile && ` -o "${session.configuration.outputFile}"`;
		terminal.sendText(`runmany ${programArg}${settingsArg}${outputArg}`);
		return new vscode.DebugAdapterInlineImplementation(new DummyDebugSession());
	}
}

export class DummyDebugSession extends DebugSession {
	protected initializeRequest(): void {
		this.sendEvent(new TerminatedEvent());
	}
}
