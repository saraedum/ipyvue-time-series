<template>
<div>
	<comm @push="push" />
	Length of buffer: {{ length }}
	<slot v-bind:x="x" v-bind:y="y">
		...
	</slot>
</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Comm from "./comm.vue";

interface IFrame {
	x: number,
	y: number,
};

@Component({
	components: { Comm },
})
export default class TimeSeries extends Vue {
	@Prop({required: false, type: Number, default: 1000}) protected history!: number;

	protected x = [] as number[];
	protected y = [] as number[];
	protected length = 0;

	protected push({ frames } : { frames: IFrame[] }) {
		this.length = frames.length;
		for (let frame of frames) {
			this.x.push(frame.x);
			this.y.push(frame.y);
		}
		this.x = this.x.slice(-this.history);
		this.y = this.y.slice(-this.history);
	}
}
</script>
