import { name } from "../../package.json";
import activate from "../activate.ts";

const plugin = {
    id: name,
    requires: [],
    activate,
    autoStart: true,
};

export default plugin;
