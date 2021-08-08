import { createApp } from "vue";
import App from "./App.vue";
import Walls from "./components/Walls.vue"
import axios from "axios";

const appInstance = createApp(App);
appInstance.use(Walls);
axios.defaults.baseURL="http://127.0.0.1:8000/"
appInstance.mount("#app");