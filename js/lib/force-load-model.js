import { DOMWidgetModel } from "@jupyter-widgets/base";

// This (trivial) model is used by the ForceLoad widget. The only purpose of
// that widget is to force the loading of our JavaScript assets so
// <time-series> gets registered with Vue.js. (A trick that we copied from
// ipyvue.)
export class ForceLoadModel extends DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: 'ForceLoadModel',
            _model_module: 'ipyvue-time-series',
            _model_module_version: '1.0.0',
        };
    }
}
