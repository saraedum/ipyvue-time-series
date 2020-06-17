import { name, version } from "../../package.json";
import { IJupyterWidgetRegistry } from "@jupyter-widgets/base";
import { Application } from '@lumino/application';
import { Widget } from '@lumino/widgets';
import View from "../view.ts";
import Model from "../model.ts";

const plugin = {
    id: name,
    requires: [IJupyterWidgetRegistry],
    activate: (app: Application<Widget>, registry: IJupyterWidgetRegistry) => registry.registerWidget({
        name,
        version,
        exports: { View, Model },
    }),
    autoStart: true,
};

export default plugin;
