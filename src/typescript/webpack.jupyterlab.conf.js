var path = require('path');
var targets = require('./webpack.notebook.conf.js');

const plugin = {
    // This bundle contains the frontend of the JupyterLab plugin. We
    // precompile this into an AMD bundle which is then picked up by JupyterLab
    // which recompiles it into its actual bundle.
    // We do not use JupyterLab bundling directly since we want to use some
    // loaders here that are not present in JupyterLab's webpack configuration.
    entry: './ipyvue-time-series/jupyterlab/plugin.ts',
    output: {
        path: path.resolve(__dirname, "dist", "jupyterlab"),
        filename: "index.js",
        libraryTarget: "amd"
    },
    devtool: "eval-source-map",
    externals: [
        /^@lumino\/.+$/,
        /^@jupyterlab\/.+$/,
        '@jupyter-widgets/base',
    ],
    module: targets[1].module,
    plugins: targets[1].plugins,
}

module.exports = [ plugin ];
