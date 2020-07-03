<template>
	<div />
</template>
<script lang="ts">
import { Component, Inject, Vue } from "vue-property-decorator";
import { Kernel, KernelMessage } from "@jupyterlab/services";

interface IViewContext {
	getModelById: (id: number) => any;
	getView: () => any;
};

interface IMessage {
	command: string;
};

@Component
export default class Comm extends Vue {
	// This object is provided by ipyvue's VueView
	@Inject()
	protected readonly viewCtx!: IViewContext;

	protected view: any;
	protected model: any;
	protected kernel!: Kernel.IKernelConnection;

	protected backend!: Kernel.IComm;
	protected target!: string;

	private comm!: Kernel.IComm;

	protected async mounted() {
		this.view = this.viewCtx.getView();
		this.model = this.view.model;
		const context = this.model.widget_manager.context;
		await context.ready;
		const sessionContext = context.sessionContext;
		await sessionContext.ready;
		this.kernel = sessionContext.session.kernel;
		
		// The backend is going to connect to this comm to send updates.
		this.target = `${this.model.attributes.target}-${this.view.cid}`;
		this.kernel.registerCommTarget(this.target, (comm: Kernel.IComm) => {
			this.comm = comm
			comm.onMsg = this.onMessage;
		});

		// We tell the backend about our comm target and subscribe to updates.
		this.backend = this.kernel.createComm(this.model.attributes.target);
		this.backend.open();
		this.backend.send({
			command: "register",
			target: this.target,
		});
	}

	private onMessage(message: KernelMessage.ICommMsgMsg) {
		const payload = message.content.data as any as IMessage;
		this.$emit(payload.command, payload);
		this.comm.send({command: "ack"})
	}
}
</script>
