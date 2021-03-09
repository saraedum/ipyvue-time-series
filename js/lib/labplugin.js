var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'ipyvue-time-series:plugin',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipyvue-time-series',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

