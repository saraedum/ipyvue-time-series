const ForceLoadModel = require('./force-load-model');
const version = require('../package.json').version;
const activate = require('./activate').activate;

module.exports = {
  ...ForceLoadModel,
  activate,
  version,
}
