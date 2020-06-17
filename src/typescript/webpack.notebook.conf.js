const path = require('path');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

const setup = {
    // This bundle contains the part of the JavaScript that is run on
    // load of the notebook. This section generally only performs
    // some configuration for requirejs, and provides the legacy
    // "load_ipython_extension" function which is required for any notebook
    // extension.
    entry: './ipyvue-time-series/notebook/setup.js',
    output: {
        filename: 'extension.js',
        path: path.resolve(__dirname, '..', 'python', 'generated', 'notebook', 'javascript'),
        libraryTarget: 'amd'
    }
};

const widget = {
    // This bundle contains the implementation for the custom widget views and
    // custom widget.
    entry: './ipyvue-time-series/notebook/widget.ts',
    output: {
        filename: 'widget.js',
        path: path.resolve(__dirname, '..', 'python', 'generated', 'notebook', 'javascript'),
        libraryTarget: 'amd'
    },
    devtool: 'source-map',
    module: {
        rules: [{
            test: /\.css$/,
            use: ['style-loader', 'css-loader'],
        }, {
            test: /\.ts$/,
            use: ['ts-loader'],
        }]
    },
    externals: [
        '@jupyter-widgets/base'
    ],
    plugins: [
        new BundleAnalyzerPlugin({ analyzerMode: 'static' })
    ],
};

module.exports = [ setup, widget ];
