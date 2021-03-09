// Resolve when the notebook is ready to create comm targets & open comms.
async function commReady(widget_manager) {
  if (widget_manager.context) {
    // JupyterLab
    const context = widget_manager.context;
    await context.ready;

    const sessionContext = context.sessionContext;
    await sessionContext.ready;
  }
}

// Register a frontend comma target in this notebook and return a promise
// that resolves to the comm once the backend has connected to it.
function registerCommTarget(widget_manager, target, callback) {
  if (widget_manager.context) {
    // JupyterLab
    const context = widget_manager.context;
    const sessionContext = context.sessionContext;
    const kernel = sessionContext.session.kernel;

    return new Promise((accept) => {
      kernel.registerCommTarget(target, (comm) => {
        comm.onMsg = callback;
        accept(comm);
      });
    });
  } else {
    // Classic Notebook
    return new Promise((accept) => {
      widget_manager.comm_manager.register_target(target, (comm) => {
        comm.on_msg(callback);
        accept(comm);
      });
    });
  }
}

// Return a comm to the backend.
function createComm(widget_manager, target) {
  if (widget_manager.context) {
    // JupyterLab
    const context = widget_manager.context;
    const sessionContext = context.sessionContext;
    const kernel = sessionContext.session.kernel;

    const comm = kernel.createComm(target);
    comm.open();
    return comm;
  } else {
    // Classic Notebook
    return widget_manager.comm_manager.new_comm(target, {});
  }
}

export default {
  // This object is provided by ipyvue's VueView
  inject: [ 'viewCtx' ],
  render() {},
  async mounted() {
    const view = this.viewCtx.getView();
    const model = view.model;
    const target = `${model.attributes.target}-${view.cid}`;
    await commReady(model.widget_manager);

    // Create a comm target that the backend can send data to.
    const commTarget = registerCommTarget(model.widget_manager, target, (msg) => this.onMessage(msg));

    // We tell the backend about our comm target.
    createComm(model.widget_manager, model.attributes.target).send({command: "register", target});

    // Wait for the backend to connect to our comm target.
    this.comm = await commTarget;
  },
  data() {
    return {
      comm: null,
    };
  },
  methods: {
    onMessage(message) {
      const payload = message.content.data;
      this.$emit(payload.command, payload);
      this.comm.send({command: "ack"});
    },
  }
}
