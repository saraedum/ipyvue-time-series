import { DOMWidgetModel } from "@jupyter-widgets/base";
import { version } from "../package.json";

export default class Model extends DOMWidgetModel {
    public defaults() {
        return Object.assign(super.defaults(), {
            _model_name : 'Model',
            _model_module : 'ipyvue-time-series',
            _model_module_version : version,
            _view_name : 'View',
            _view_module : 'ipyvue-time-series',
            _view_module_version : version,
        });
    }
}
