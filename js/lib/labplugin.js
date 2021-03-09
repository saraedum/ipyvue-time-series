const plugin = require('./plugin');
const base = require('@jupyter-widgets/base');

module.exports = {
  id: 'ipyvue-time-series:plugin',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      plugin.activate(app, widgets);
      widgets.registerWidget({
          name: 'ipyvue-time-series',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};
