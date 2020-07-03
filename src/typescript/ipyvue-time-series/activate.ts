import Vue from "vue";
import TimeSeries from "./time-series.vue";

export default function activate() {
    Vue.component('time-series', TimeSeries);
}
