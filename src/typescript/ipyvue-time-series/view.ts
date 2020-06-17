import { DOMWidgetView } from "@jupyter-widgets/base";

export default class View extends DOMWidgetView {
    public render() {
        this.el.textContent = "Hello World";
    }
}
