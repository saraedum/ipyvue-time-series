import { Vue } from "jupyter-vue";
import TimeSeries from "./time-series";

export function activate(app, widget) {
  // Register <time-series/> as a tag with Vue.js.
  Vue.component("time-series", TimeSeries);
}
