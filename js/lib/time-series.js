import Comm from "./comm";

export default {
  template: `
  <div>
    <comm @push="push" />
    <slot v-bind:x="x" v-bind:y="y">
      …
    </slot>
  </div>
  `,
  components: { Comm },
  props: {
    history: {
      required: false,
      type: Number,
      default: 1000,
    },
  },
  data() {
    return {
      x: [],
      y: [],
    };
  },
  methods: {
    push({ frames }) {
      for (let frame of frames) {
        this.x.push(frame.x);
        this.y.push(frame.y);
      }
      this.x = this.x.slice(-this.history);
      this.y = this.y.slice(-this.history);
    },
  },
};
